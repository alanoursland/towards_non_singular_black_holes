## Why #3 Is Easiest to Partially Address

1. **Straightforward Setup.**  
   Whereas deriving a local radiation function from full quantum field theory (#1) or fully coupling quantum backreaction into Einstein’s equations (#2) requires deep quantum-gravitational machinery, *setting up* a self-consistent conservation law involves more standard tools of classical field theory and hydrodynamics.

2. **Simple Integral/Flux Approach.**  
   The paper sketches an energy balance like  
   \[
     \int_0^{r_s} \frac{\partial M(r,t)}{\partial t} \, dr \;=\; -\,\int_0^{r_s} \Gamma_H(r,t)\,dr,
   \]  
   or its variation  
   \[
     \int_0^{r_c} \Gamma_H(r)\,dr \;=\;\int_0^{r_c} \Phi_{\text{collapse}}(r)\,dr,
   \]  
   which is more approachable than, say, deriving the local emission rate *ab initio* from quantum field theory. You can impose physically motivated constraints (like local energy-momentum conservation) and see what the fluxes must satisfy without having to solve the entire problem at the Planck scale.

3. **Less Dependent on Unsettled Physics.**  
   The core balance condition is primarily a statement of energy continuity. It does not require a fully worked-out quantum theory of Hawking-like pair production at each radius, only a schematic function \(\Gamma_H(r)\) and a notion of inward flux \(\Phi_{\mathrm{collapse}}(r)\). Hence it’s well suited to a *partial* solution, where you can hypothesize forms for \(\Gamma_H(r)\) and \(\Phi_{\mathrm{collapse}}(r)\) and check whether consistent integrals exist.

---

## Outline of a Partial Solution for #3

Below is a sketch of how one might partially solve the self-consistency requirement for radiation versus collapse:

1. **Set Up the Conservation Equation.**  
   - Assume a spherically symmetric interior with enclosed mass-energy \(M(r,t)\).  
   - Let \(\Gamma_H(r,t)\) be the local emission rate (energy per unit time per radial shell).  
   - Let \(\Phi_{\mathrm{collapse}}(r,t)\) be the net inward mass-energy flux.  

   A simplified 1D (in \(r\)) conservation law can look like:  
         \[
         \frac{\partial M(r,t)}{\partial t} 
         \;+\;
         \frac{\partial \Phi(r,t)}{\partial r} 
         \;=\; 
         -\,\Gamma_H(r,t),
         \]  

   where \(\Phi(r,t)\) is the net (outward minus inward) flux. At equilibrium, \(\partial M(r,t)/\partial t = 0\), so this reduces to  
         \[
         \frac{\partial \Phi(r)}{\partial r} 
         = 
         -\,\Gamma_H(r).
         \]


2. **Impose an Equilibrium Condition.**  
   In an equilibrium core, the matter density stops collapsing (inward velocity goes to zero), so we can say \(\Phi_{\mathrm{collapse}}(r) \approx 0\) inside \(0 \le r \le r_c\). At the same time, \(\Phi_{\mathrm{total}}(r)\) must balance out \(\Gamma_H(r)\). Integrating from \(0\) to \(r_c\) gives:  
         \[
         \Phi(r_c) - \Phi(0) 
         = 
         - \int_0^{r_c} \Gamma_H(r)\,dr.
         \]  
   We can define boundary conditions, say \(\Phi(0)=0\) at the center. Hence  
   \[
   \Phi(r_c) = - \int_0^{r_c} \Gamma_H(r)\,dr.
   \]  
   Interpreted physically, the net outward flux through radius \(r_c\) just counters the integrated emission rate inside that radius.

3. **Pick a Toy Model for \(\Gamma_H(r)\).**  
   To partially solve the system, you can propose a simple curvature-driven form. For instance,  
   \[
   \Gamma_H(r) \;=\; \kappa \,R(r),
   \]  
   where \(\kappa\) is a constant and \(R(r)\) is the Ricci scalar or a proxy for “local curvature.” If you also hypothesize a constant-curvature interior (\(R(r)=R_c\) for \(r \le r_c\)), then \(\Gamma_H\) is uniform inside the core: \(\Gamma_H = \kappa R_c\). Then the net flux from the center to \(r_c\) is simply \(\kappa R_c\,r_c\).  

4. **Solve for \(r_c\) or \(R_c\).**  
   One can tie \(R_c\) to the energy density via Einstein’s equations (e.g., \(R_c \sim 8\pi G\rho_c\)) and require that the black hole mass enclosed by \(r_c\) matches the “pressure” of this local emission. Though still heuristic, this exercise clarifies how \(\Gamma_H(r)\) and \(\Phi_{\mathrm{collapse}}(r)\) must be related for equilibrium.

5. **Refine Step by Step.**  
   - Insert more realistic forms of \(\Gamma_H(r)\) that grow with \(R(r)\).  
   - Explore a radial dependence for \(\rho(r)\).  
   - Impose boundary conditions at \(r_s\) (the event horizon) for continuity with external Hawking flux.  

Even this stripped-down partial approach illuminates how (i) specifying a *local* radiation law, (ii) imposing energy conservation, and (iii) setting boundary conditions could yield non-singular, finite-radius solutions under certain assumptions.

---

Below is a concise set of **open questions** that remain in challenge **#3 (Establish a Self-Consistent Conservation Law and Balance Condition)** even after attempting a partial solution or toy model.

---

## 1. Exact Functional Dependence of Radiation on Curvature

- **Heuristic vs. First Principles**  
  Even if one posits a local function \(\Gamma_H(r)\) that scales with curvature (e.g., \(\Gamma_H \propto R(r)\)), the **true** functional dependence must come from a robust quantum field theoretic or quantum gravity derivation. A purely guessed or phenomenological form leaves the model’s predictive power uncertain.  

- **Incorporating Negative-Energy Partners**  
  Standard Hawking radiation arguments invoke negative-energy partners falling inward. It’s unclear *how* those negative-energy components figure into the local balance condition \(\Gamma_H(r) - \Phi_{\text{collapse}}(r)=0\). Ensuring energy-momentum conservation locally requires a fully specified stress-energy tensor for both positive- and negative-energy fluxes.

---

## 2. Coupling to the Metric and Einstein’s Equations

- **Metric Backreaction**  
  The partial solution typically treats \(\Gamma_H(r)\) and \(\Phi_{\mathrm{collapse}}(r)\) as separate functions. However, in a *real* self-consistent solution, each of these fluxes alters the spacetime metric, which in turn alters \(\Gamma_H(r)\). A fully covariant treatment must solve (modified) Einstein equations  
  \[
    G_{\mu\nu} \;=\; 8 \pi G \, \bigl(T_{\mu\nu}^\text{matter} + T_{\mu\nu}^\text{radiation}\bigr),
  \]  
  where \(T_{\mu\nu}^\text{radiation}\) must be derived from the local emission/absorption processes.  

- **Boundary Conditions**  
  Even if one can write down an energy conservation law, setting consistent boundary conditions at both \(r=0\) (the core) and \(r=r_s\) (the horizon) can be tricky. The partial solution might impose \(\Phi(0)=0\) by fiat and continuity at \(r_s\), but the interplay between the exterior (horizon-level) Hawking flux and the interior flux remains poorly understood.

---

## 3. Time-Dependent (Non-Equilibrium) Dynamics

- **Beyond Stationary Solutions**  
  The core approach to #3 often looks at “equilibrium” or “steady-state” conditions, but real black holes evolve in time (they evaporate). Demonstrating that an equilibrium *can* exist at a given moment is different from showing that the system actually *relaxes* to it through dynamical evolution.

- **Nonlinear Instabilities**  
  If \(\Gamma_H(r)\) is too weak or saturates too quickly, or if \(\Phi_{\mathrm{collapse}}(r)\) grows under perturbations, the black hole might still form a singularity or depart from equilibrium in a more violent way. Thus, one must test whether the solution is stable under time-dependent fluctuations.

---

## 4. Physical Meaning of the Flux \(\Phi_{\mathrm{collapse}}(r)\)

- **Defining “Collapse Flux”**  
  The partial solution sketches \(\Phi_{\mathrm{collapse}}(r)\) as an inward flow of matter or mass-energy. However, in a strong-gravity regime with curvature-driven pair creation, matter does not simply move as a classical fluid. One must clarify how \(\Phi_{\mathrm{collapse}}\) arises from the underlying matter fields, their equations of state, or from negative-energy states.

- **Matching to a Realistic Matter Model**  
  In astrophysical or theoretical contexts, black holes may contain collapsing stellar material, quantum fields, or both. Specifying each contribution to \(\Phi_{\mathrm{collapse}}(r)\) requires either a fluid approximation (e.g., perfect fluid with an equation of state) or a quantum field approach. Pinning this down remains an open question.

---

## 5. Integrating With the Outer Hawking Process

- **Consistency Across \(r = r_s\)**  
  Traditional Hawking emission is governed by horizon-scale physics, while this challenge #3 deals primarily with *interior* fluxes and local radiation. Ensuring a single, globally consistent solution means matching the interior solution to the exterior flux:  
  \[
    \Gamma_{\text{int}}(r_s) 
      \; \overset{?}{=}\;
    \Gamma_{\text{ext}}(\text{standard Hawking}),
  \]  
  or determining whether the two are wholly distinct effects.  

- **Mass Evolution**  
  As external Hawking radiation reduces the black hole mass, the Schwarzschild radius \(r_s\) decreases. One must update both \(\Gamma_H(r)\) and the collapse flux accordingly. This couplings leads to a time-varying interior boundary at \(r_s(t)\), further complicating the conservation law.

---

## 6. Role in the Information Paradox

- **Information Flow**  
  Even if the local balance condition \(\Gamma_H(r)\approx \Phi_{\mathrm{collapse}}(r)\) prevents a singularity, it does not address *how* quantum information might be encoded in these fluxes or eventually returned to the outside universe.  
- **Microstate Counting and Unitarity**  
  A self-consistent balance is not necessarily a unitarity solution. Does this partial approach to #3 require new constraints if one demands that no information is lost? That open question ties into deeper issues of quantum gravity.

---

## 7. Numerical Implementation and Simulations

- **Practical Computation**  
  Deriving a partial or toy solution on paper is one thing, but a 1D or 2D simulation that evolves the system from initial collapse to an equilibrium (or near-equilibrium) state would offer more robust evidence.  
- **Multi-Field Complexity**  
  Realistic black holes could contain multiple fields (e.g., electromagnetic fields, scalar fields, standard model fermions). Modeling each field’s contribution to \(\Gamma_H(r)\) or \(\Phi_{\mathrm{collapse}}(r)\) can escalate the complexity significantly.

---

### Summary

Even after setting up a **partial** or **toy** version of the local conservation law and flux balance, **major open questions** remain about:

1. The precise **functional form** of \(\Gamma_H(r)\).  
2. **Coupling** this flux-based description to Einstein’s field equations.  
3. Realistic **time-dependent and nonlinear** dynamics.  
4. The physical **origin and nature** of the inward flux \(\Phi_{\mathrm{collapse}}\).  
5. **Matching** with the standard horizon-level Hawking process.  
6. Possible **information** and unitarity constraints.  
7. **Practical** numerical simulation strategies.

Answering these would move the approach from a schematic energy-balance argument toward a fully self-consistent, predictive theory of non-singular black holes.