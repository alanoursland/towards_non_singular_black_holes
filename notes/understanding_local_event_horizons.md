### Understanding "Local Event Horizons" in the Black Hole Interior

Your perspective in the paper—that every radial distance \( r \) between the event horizon (\( r_s = 2M \), in units where \( G = c = \hbar = 1 \)) and the center (\( r = 0 \)) can be treated as a "local event horizon"—is an intriguing speculative extension of standard ideas. However, in rigorous general relativity (GR) and quantum field theory in curved spacetime (QFTCS), the event horizon is a **global** feature: it's the null surface beyond which null geodesics (light rays) cannot escape to future null infinity (\( \mathcal{I}^+ \)). There are no true "local event horizons" at arbitrary \( r < r_s \); instead, the interior contains **trapped surfaces** (regions where both ingoing and outgoing null geodesics converge toward the singularity), but these don't function like horizons for radiation production in the same way.

That said, your idea aligns with some modern research on how quantum effects (like Hawking radiation) manifest **inside** the black hole, as perceived by local observers. Hawking radiation itself is a global semiclassical effect, derived from mode mixing across the entire spacetime during collapse. But we can generalize it to **local perceptions** using tools like Unruh-DeWitt (UDW) detectors (which model particle detectors coupling to quantum fields) or by considering observer-dependent thermal baths via the Unruh effect. These show that observers at different \( r \) inside do perceive thermal radiation that varies with position, though it's not due to "local horizons" but rather curvature-induced vacuum excitations and redshift factors.

I'll set up the mathematical framework below, drawing from standard derivations and recent papers (e.g., on freely falling detectors inside black holes). This neither fully proves nor disproves your heuristic—it's speculative, as your paper notes—but it shows how to formalize it. The math supports a position-dependent "Hawking-like" effect inside, which could inspire your curvature-dependent rate \( \Gamma_R(r) = f(\mathcal{R}(r)) \). However, in standard theory, this interior radiation doesn't escape or balance collapse; it's trapped and contributes to the singularity unless quantum gravity (QG) modifies it.

### Step 1: Challenges with "Local Event Horizons" Inside
- **Spacetime Structure Inside**: In Schwarzschild coordinates, the metric inside (\( r < 2M \)) is \( ds^2 = (2M/r - 1) dt^2 - (2M/r - 1)^{-1} dr^2 + r^2 d\Omega^2 \). Here, \( r \) is time-like (inevitable infall to \( r=0 \)), and \( t \) is space-like. No static observers exist; all are infalling. The curvature (e.g., Kretschmann scalar \( K = 48M^2 / r^6 \)) diverges at \( r=0 \), but there's no horizon-like surface at each \( r \).
- **No Local Horizons**: Apparent horizons (local trapped surfaces) exist at \( r=2M \), but inside, the region is fully trapped. To mimic "local horizons," we can use **Rindler-like approximations** (local accelerated frames) or embed the metric to compute local Unruh temperatures, treating high-curvature regions as inducing thermal effects.
- **Observer Frames**: We'll use **freely falling (inertial) observers** (proper acceleration \( a=0 \)), as in geodesic motion, since static frames aren't possible inside. For comparison, outside, static observers at fixed \( r > 2M \) have \( a = (M/r^2) / \sqrt{1 - 2M/r} \), seeing a local temperature \( T_{\text{loc}} = T_H / \sqrt{1 - 2M/r} \) (diverging at \( r \to 2M^+ \)), where \( T_H = 1/(8\pi M) \).

### Step 2: Setting Up Observer Frames for Interior Radiation
To derive Hawking-like effects, use QFTCS with a UDW detector: a two-level quantum system (ground |g⟩, excited |e⟩ with gap \( E \)) coupled to a massless scalar field \( \phi \) (simplifying photons/gravitons). The detector follows a trajectory \( x(\tau) \) (proper time \( \tau \)), and its response measures excitations from the vacuum, indicating perceived particles.

- **Vacuum States**: 
  - **Hartle-Hawking (HH) Vacuum**: Thermal equilibrium at \( T_H \), analytic across the horizon.
  - **Unruh Vacuum**: Mimics collapse; vacuum for ingoing modes, thermal for outgoing.
  - **Boulware Vacuum**: Empty far away but singular at horizon.

For interior observers, use Kruskal-Szekeres (KS) coordinates to cover the horizon smoothly: \( U = -4M e^{-u/4M} \), \( V = 4M e^{v/4M} \) (null coordinates \( u = t - r^* \), \( v = t + r^* \), tortoise \( r^* = r + 2M \ln|r/2M - 1| \)). Inside (Region II), \( U > 0 \), \( V > 0 \), \( UV > (4M)^2 \).

- **Freely Falling Observer Trajectory**: Geodesic from rest at infinity: \( dr/d\tau = -\sqrt{2M/r + \epsilon^2 - 1} \) (energy parameter \( \epsilon =1 \) for at-rest). Proper time \( \tau(r) \) integrates this. Parameterize detector at mid-point \( r_0 < 2M \), switching on for duration \( \Delta\tau \).

### Step 3: Mathematical Derivation of Local Hawking-Like Effect
From recent work (e.g., [arXiv:2401.06609](https://arxiv.org/pdf/2401.06609) on falling UDW near/inside horizon), we can compute the detector's **excitation rate** \( F(E) \), which reveals a position-dependent perceived temperature.

#### Response Function
The probability of excitation (perceived particle flux) is \( F(E) = \lambda^2 \int_{-\infty}^\infty d\Delta\tau \, e^{-iE\Delta\tau} W(\tau, \tau + \Delta\tau) \), where \( \lambda \) is coupling, and \( W \) is the Wightman function \( \langle \phi(x(\tau)) \phi(x(\tau')) \rangle \) in the vacuum.

For HH vacuum (thermal inside), near-horizon approximation (using KS):
\[
W(U,V;U',V') \approx -\frac{1}{4\pi} \ln\left( \frac{(U-U')(V-V') + i\epsilon}{\sigma_0} \right),
\]
pulled back to the trajectory. For full computation (summing modes \( \ell, m \)):
\[
F = \sum_{\text{modes}} \int_0^\infty d\omega \, |\hat{\chi}(\omega)|^2 \left| \int d\tau \, e^{i\omega \Phi(\tau) } \chi(\tau) e^{-i\omega \tau \right|^2,
\]
where \( \Phi(\tau) \) is phase from mode functions (e.g., \( e^{-i\omega U} \) for outgoing), \( \chi(\tau) \) is switching (e.g., Gaussian \( e^{-\tau^2 / 2\sigma^2} \)).

Numerical/symbolic evaluation (as in papers) shows:
- Outside (\( r > 2M \)): \( F(E) \) corresponds to graybody Planck spectrum at \( T_{\text{eff}} \approx T_H (1 + M/r + \dots) \).
- At horizon (\( r = 2M \)): \( T_{\text{eff}} \to 2 T_H \) (smooth crossing).
- Inside (\( r < 2M \)): \( F(E) \) **increases** continuously, with \( T_{\text{eff}} > 2 T_H \), rising as \( T \approx T_H \sqrt{1 + (2M/r) + (2M/r)^2 + (2M/r)^3} \) (from 6D embedding, where local acceleration \( a \) in higher dims mimics curvature).

This is derived by solving the detector's 6D acceleration \( a(r) \) and using Unruh formula \( T = a / (2\pi) \).

#### Effective Temperature Derivation
Embed Schwarzschild in 6D Minkowski: Coordinates satisfy flat metric, yielding local \( a(r) = M (1 + 3(2M/r)/2) / (r^2 \sqrt{1 - 2M/r}) \) outside; analytically continue inside by flipping signs. Then \( T(r) = a(r) / (2\pi) \), which is finite and increasing inside, supporting your local \( f(\mathcal{R}) \) (since \( \mathcal{R} \propto 1/r^3 \) Ricci, but better Kretschmann \( \propto 1/r^6 \)).

For Kerr (rotating BH), similar: Temp regular at outer horizon, negative/divergent at inner (Cauchy) horizon, varying with observer class.

#### Bogoliubov for Interior Generalization
Hawking's original: Modes from past infinity mix via \( \beta_{\omega\omega'} \neq 0 \), yielding \( N_\omega = 1/(e^{8\pi M \omega} - 1) \). Interior modes \( \phi^{\text{int}} \) carry negative energy but don't contribute to outgoing flux. To localize: Use wave packets centered at \( r_0 < 2M \), but causality prevents "local derivation"—effects require global structure.

Tunneling alternative (Parikh-Wilczek): Emission rate \( \Gamma \propto e^{-2 \Im I} \), action \( I = \int p dr \), semiclassical across "local barriers." Inside, pair creation can be approximated locally, with rate \( \Gamma \sim e^{- \pi E^2 / a(r)} \), where \( a(r) \) is local tidal acceleration, yielding thermal spectrum \( T \propto \sqrt{\mathcal{R}(r)} \).

### Step 4: Prove or Disprove?
- **Partial Proof**: Yes, observers at different \( r < 2M \) perceive Hawking-like thermal radiation, with temperature varying locally (increasing toward singularity). Papers show smooth, position-dependent \( T(r) \) inside via UDW detectors. This supports your \( \Gamma_R(r) \propto f(\mathcal{R}(r)) \), e.g., \( f \propto \sqrt{K} \propto 1/r^3 \).
- **Disproof Aspects**: It's not from "local event horizons"—no such structures exist at each \( r \). The effect is global (horizon formation causes vacuum mismatch), and interior radiation is trapped (no escape, no self-regulation in standard GR/QFTCS). For balance, need QG backreaction (e.g., loop quantum gravity bounces).
- **Implications for Your Model**: Formalize as local Unruh from tidal forces: \( T(r) = \sqrt{|\nabla^2 \phi_{\text{grav}}| / (2\pi)} \approx \sqrt{M / r^3} / (2\pi) \), where \( \phi_{\text{grav}} \) is Newtonian potential analog. This could derive your \( f(\mathcal{R}) \).
