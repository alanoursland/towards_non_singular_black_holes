import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------
# 1. Model Parameters (Planck units)
# ----------------------------------------------------------------------

N_s, N_f, N_v = 1, 2, 1
alpha = (N_s + 6*N_f + 12*N_v) / (3840 * np.pi**2)
C_emission = 6.1e-4
epsilon_threshold = 1e-3
K_th = epsilon_threshold  # Planck units

# ----------------------------------------------------------------------
# 2. Domain and Mesh
# ----------------------------------------------------------------------

tol=1e-4
x_min, x_max = 1e-6, 1.0
n_points = 300
# x_mesh = np.linspace(x_min, x_max, n_points)
x_mesh = np.logspace(np.log10(x_min), np.log10(x_max), n_points)

# ----------------------------------------------------------------------
# 3. Physics Functions
# ----------------------------------------------------------------------

def Gamma_H(K_actual):
    K_safe = np.maximum(K_actual, 1e-12)
    gamma_val = np.where(K_safe >= K_th,
                         C_emission * (K_safe / K_th)**0.75,
                         0.0)
    return np.clip(gamma_val, 0.0, 1e-2)  # Cap emission rate

def compute_kretschmann(x, mu, phi_prime):
    """
    Kretschmann scalar K for a metric 
      ds^2 = -e^{-2φ}f dt^2 + dr^2/f + r^2 dΩ^2,
    with r = 2 x and f = 1 − 2μ/r.
    """
    r = 2.0 * x
    m = mu
    f = 1.0 - 2.0 * m / r

    # Classical piece: 48 M^2 / r^6
    K0 = 48.0 * m**2 / r**6

    # Correction from φ′ (and, if desired, you can add f′ or φ″ terms here)
    corr = 1.0 + 12.0 * r * phi_prime**2 / (f + 1e-10) + 6.0 * r**2 * phi_prime**2

    return K0 * corr

def dmu_dx(x, rho_total):
    """
    dμ/dx = 4π r^2 ρ · (dr/dx)
           = 4π (2x)^2 ρ · 2 = 32 π x^2 ρ
    """
    return 32.0 * np.pi * x**2 * rho_total

def dphi_dx(x, mu, p_total):
    """
    dφ/dx = 2 · [ (m/r + 4π r^2 p) / (r f) ],
    with r = 2x, f = 1 − 2m/r.
    """
    r = 2.0 * x
    m = mu
    f = 1.0 - 2.0 * m / r
    denom = r * f + 1e-10

    return np.where(
        np.abs(f) > 1e-10,
        2.0 * (m / r + 4.0 * np.pi * r**2 * p_total) / denom,
        0.0
    )

def bc_residual(ya, yb):
    mu_a, phi_a, mu_pa, phi_pa = ya
    mu_b, phi_b, mu_pb, phi_pb = yb

    # recompute A,B from the anomaly at x_min
    rho0, p0 = compute_anomaly_stress(x_min, 0.0, alpha)
    A = (32.0 * np.pi / 3.0) * rho0
    B = 8.0 * np.pi * p0

    return np.array([
        mu_a    - A * x_min**3,   # series for μ at left boundary
        phi_pa  - 2.0 * B * x_min,# series for φ' at left boundary
        mu_b    - 0.5,            # Schwarzschild mass at outer boundary
        phi_b                  # gauge at outer boundary
    ])

def compute_anomaly_stress(x, mu, alpha, H2_max=10.0):
    """
    Simple toy conformal‑anomaly model:
      H^2 ∼ m / r^3  ⇒  ρ_anom = 6α H^4  (or adjust power to taste)
    Here we cap H^2 to [0, H2_max] and use p = ρ/3.
    """
    r = 2.0 * x
    m = mu

    # Effective H^2, dimensionally H^2 ~ m / r^3
    H2_eff = np.clip(m / r**3, 0.0, H2_max)

    # Anomaly energy density and pressure (radiation‑like)
    rho_anom = 6.0 * alpha * H2_eff**2
    p_anom   = rho_anom / 3.0

    return rho_anom, p_anom

def compute_emission_rate(K, C_emission, K_th, gamma_max=1e-2):
    """
    Emission rate Γ ∼ C (K/K_th)^0.75, clipped at γ_max.
    """
    K_safe = np.maximum(K, 1e-20)
    gamma_val = C_emission * (K_safe / K_th)**0.75
    return np.clip(gamma_val, 0.0, gamma_max)

# ----------------------------------------------------------------------
# 4. Differential System and Boundary Conditions
# ----------------------------------------------------------------------

def series_initial_conditions(x_min, alpha, phi0=0.0):
    """
    Compute [μ, φ, μ′, φ′] at x = x_min via the small‑x power series,
    but evaluate the anomaly stress at x_min rather than at zero.
    """
    # (a) get the anomaly stress safely at x_min
    rho0, p0 = compute_anomaly_stress(x_min, 0.0, alpha)

    # (b) series coefficients from dμ/dx ≃ 32π x^2 ρ0  and  dφ/dx ≃ 16π p0 x
    A = (32.0 * np.pi / 3.0) * rho0      # so μ(x) ≃ A x^3
    B = 8.0  * np.pi * p0               # so φ(x) ≃ φ0 + B x^2

    # (c) initial values at x_min
    mu0    = A * x_min**3
    phi0_i = phi0 + B * x_min**2
    mu_p0  = 3.0 * A * x_min**2
    phi_p0 = 2.0 * B * x_min

    return np.array([mu0, phi0_i, mu_p0, phi_p0])

def ode_system(x, y):
    mu, phi, mu_prime, phi_prime = y

    # 1) curvature
    K = compute_kretschmann(x, mu, phi_prime)

    # 2) anomaly stress (radiation‑like, p = ρ/3)
    rho_anom, p_anom = compute_anomaly_stress(x, mu, alpha)

    # 3) quantum emission
    rho_H = compute_emission_rate(K, C_emission, K_th)
    p_H   = rho_H

    # 4) total fluid
    rho_tot = rho_anom + rho_H
    p_tot   = p_anom   + p_H

    # 5) ODEs
    dmu   = dmu_dx(x, rho_tot)               # =32π x² ρ_tot
    dphi  = dphi_dx(x, mu, p_tot)            # includes the factor of 2

    return [mu_prime, phi_prime, dmu, dphi]

def bc_residual(ya, yb):
    """
    ya = [μ(x_min), φ(x_min), μ'(x_min), φ'(x_min)]
    yb = [μ(1),     φ(1),     μ'(1),     φ'(1)    ]
    """
    mu_a, phi_a, mu_pa, phi_pa = ya
    mu_b, phi_b, mu_pb, phi_pb = yb

    # recompute the same A and B used above, at x_min
    rho0, p0 = compute_anomaly_stress(x_min, 0.0, alpha)
    A = (32.0 * np.pi / 3.0) * rho0
    B = 8.0  * np.pi * p0

    return np.array([
        mu_a    - A * x_min**3,    # μ(x_min) = A x_min^3
        phi_pa  - 2.0 * B * x_min, # φ'(x_min) = 2 B x_min
        mu_b    - 0.5,             # match M(r_s)=½
        phi_b                      # φ(1)=0 gauge
    ])

def initial_guess(x):
    mu = 0.5 * x**3
    phi = -0.05 * x**2
    mu_prime = 1.5 * x**2
    phi_prime = -0.1 * x
    return np.array([mu, phi, mu_prime, phi_prime])

# ----------------------------------------------------------------------
# 5. Solve and Visualize
# ----------------------------------------------------------------------

print("Attempting to solve BVP...")

y0_left = series_initial_conditions(x_min, alpha, phi0=0.0)
y_guess = np.tile(y0_left[:,None], (1, x_mesh.size))
sol = solve_bvp(
    ode_system,
    bc_residual,
    x_mesh,
    y_guess,
    max_nodes=500000, tol=tol, verbose=2
)

if sol.success:
    print("✅ BVP solver succeeded!")
else:
    print("❌ BVP solver failed:", sol.message)

# Classical curvature profile: K_classical = 48 / (r^6) = 48 / (2x)^6
x_vals = np.logspace(np.log10(x_min), np.log10(x_max), 300)
kappa_classical = 48.0 / ((2 * x_vals)**6 * K_th)  # normalized K / K_th

# Optional: plot the initial guess and solution for mu(x)
plt.figure(figsize=(6, 4))
if sol.success:
    plt.loglog(x_vals, kappa_classical, 'k--', label='Classical $K \\propto r^{-6}$')
    # plt.xlim(1e-4, 1)
    # plt.ylim(1e5, 1e27)  # Match the quantum y-range
    plt.ylim(bottom=1)


plt.xlabel('$x = r / r_s$')
plt.ylabel(r'$\kappa(x) = K / K_{\mathrm{th}}$')
plt.title('Curvature Profile (Classical)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("results/Kprofile_classic_only.png", dpi=300)
plt.savefig("results/Kprofile_classic_only.pdf", dpi=300)
# plt.show()

# ----------------------------------------------------------------------
# 6. Compute and Plot κ(x) = K / K_th
# ----------------------------------------------------------------------

print("🔄 Computing normalized curvature profile κ(x) = K / K_th...")

def compute_kappa_array(x_vals, mu_vals, phi_vals, mu_prime_vals, phi_prime_vals, K_th):
    """
    Returns κ(x) = K(x) / K_th for each point in the solution arrays.
    Only x, μ and φ' are needed by compute_kretschmann.
    """
    # vectorized call: compute_kretschmann accepts array inputs
    K_vals = compute_kretschmann(x_vals, mu_vals, phi_prime_vals)
    return K_vals / K_th

# Extract from BVP solution
x_sol = sol.x
mu_sol = sol.y[0]
phi_sol = sol.y[1]
mu_prime_sol = sol.y[2]
phi_prime_sol = sol.y[3]

# Compute κ(x)
kappa_array = compute_kappa_array(
    x_sol,
    mu_sol,
    phi_sol,
    mu_prime_sol,
    phi_prime_sol,
    K_th
)

print(f"✅ κ(x) computed at {len(x_sol)} points.")

# Classical comparison curve
x_classical = np.logspace(np.log10(x_min), np.log10(x_max), 200)
kappa_classical = 48.0 / ( (2*x_classical)**6 * K_th )

# Estimate core radius (curvature plateau)
dlogK_dlogx = np.gradient(np.log(kappa_array), np.log(x_sol))
idx_core = np.where((x_sol < 0.1) & (np.abs(dlogK_dlogx) < 1.0))[0]

if len(idx_core) > 0:
    x_core = x_sol[idx_core[-1]]
    kappa_core = kappa_array[idx_core[-1]]
    print(f"📍 Core radius detected: x_c ≈ {x_core:.4f}, κ_c ≈ {kappa_core:.2f}")
else:
    x_core = 0.05
    kappa_core = kappa_array[np.searchsorted(x_sol, x_core)]
    print("⚠️ No curvature plateau detected. Using fallback x_c = 0.05")
    
np.savetxt("results/kappa_profile.dat", np.column_stack([x_sol, kappa_array]), header="x     kappa", comments="# ")

print(f"x_sol range: {x_sol.min():.2e} to {x_sol.max():.2e}")
print(f"kappa_array range: {np.nanmin(kappa_array):.2e} to {np.nanmax(kappa_array):.2e}")
print(f"Any NaNs? {np.isnan(kappa_array).any()}")
print(f"Any Infs? {np.isinf(kappa_array).any()}")

print("📁 Saved data to kappa_profile.dat")

print("📊 Ready to plot curvature profile.")

# Plot only the quantum-corrected curvature profile
plt.figure(figsize=(6, 4))
plt.loglog(x_sol, kappa_array, 'b-', linewidth=2, label=r'$\kappa(x)$ (quantum-corrected)')

# Threshold line: κ = 1
plt.axhline(y=1.0, color='gray', linestyle=':', linewidth=1)
plt.text(0.3, 1.2, r'$\kappa = 1$', fontsize=10)

# Mark core radius, even if fallback
plt.axvline(x=x_core, color='gray', linestyle=':', linewidth=1)
plt.text(x_core * 1.1, kappa_core * 0.8, r'$x_c$', fontsize=10)

# Labels and formatting
plt.xlabel(r'$x = r / r_s$', fontsize=12)
plt.ylabel(r'$\kappa = K / K_{\mathrm{th}}$', fontsize=12)
plt.title("Curvature Profile (Quantum)", fontsize=12)
# plt.xlim(1e-3, 1)
# plt.ylim(0.1, 1e3)
# plt.ylim(1e5, 1e27)
# plt.ylim(min(kappa_array)*0.8, max(kappa_array)*1.2)
plt.ylim(bottom=1)

plt.grid(True, which='both', alpha=0.3)
plt.legend(frameon=False)
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Save and show
plt.savefig("results/Kprofile_quantum_only.png", dpi=300)
plt.savefig("results/Kprofile_quantum_only.pdf", dpi=300)
# plt.show()


# ----------------------------------------------------------------------
# 7. Combined Plot: Classical vs Quantum Curvature Profile
# ----------------------------------------------------------------------

plt.figure(figsize=(6, 4))

# Plot quantum-corrected κ(x)
plt.loglog(x_sol, kappa_array, 'b-', linewidth=2, label=r'Quantum-corrected $\kappa(x)$')

# Plot classical scaling κ(x) ∝ x^{-6}
plt.loglog(x_classical, kappa_classical, 'k--', linewidth=1.5, label=r'Classical $\propto x^{-6}$')

# Threshold line: κ = 1
plt.axhline(y=1.0, color='gray', linestyle=':', linewidth=1)
plt.text(0.25, 1.2, r'$\kappa = 1$', fontsize=10)

# Core radius marker
plt.axvline(x=x_core, color='gray', linestyle=':', linewidth=1)
plt.text(x_core * 1.1, kappa_core * 0.8, r'$x_c$', fontsize=10)

# Labels and layout
plt.xlabel(r'$x = r / r_s$', fontsize=12)
plt.ylabel(r'$\kappa = K / K_{\mathrm{th}}$', fontsize=12)
plt.title("Curvature Profile: Classical vs Quantum", fontsize=12)
# plt.xlim(1e-4, 1)
# plt.ylim(1e5, 1e27)
plt.ylim(bottom=1)
plt.grid(True, which='both', alpha=0.3)
plt.legend(frameon=False, fontsize=10)
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Save combined figure
plt.savefig("results/Kprofile_combined.png", dpi=300)
plt.savefig("results/Kprofile_combined.pdf", dpi=300)
print("📁 Saved combined plot to results/Kprofile_combined.pdf")
