## 1. Motivation and Context

One of the deepest puzzles in black hole physics is the **information paradox**:  
- **Hawking’s semiclassical calculation** suggests that black holes radiate in a purely thermal (or near-thermal) manner, ultimately evaporating away and leaving no imprint of the states that collapsed to form them.  
- **Quantum mechanics (unitarity)** demands that information cannot be destroyed: the global wavefunction should evolve via a unitary operator, preserving total quantum information.

\[
\text{Paradox: How can Hawking-like emission be both (i) apparently thermal and (ii) unitary?}
\]

In the **self-regulating black hole** scenarios (or other non-singular models), the interior no longer collapses into a classical singularity. If the interior remains a well-defined quantum region, perhaps it can store or re-emit information in subtle ways. Below, we **partially** sketch how one might approach quantum state evolution in that interior, thereby addressing the paradox.

---

## 2. Key Ingredients and Strategies

### 2.1 Interior Quantum States

We treat the black hole interior as a region with finite curvature, hosting:
1. **Matter fields** that originally collapsed.  
2. **Locally generated radiation** (from a curvature-dependent emission law).  
3. **Potential quantum gravitational degrees of freedom** near or above the Planck scale.

We must define how these degrees of freedom combine into a **global Hilbert space** \(\mathcal{H}\), then specify the unitary evolution operator \(U(t)\). The biggest conceptual obstacle is that **standard QFT** in a region with a horizon is typically incomplete for describing interior states plus external Hawking flux in a globally unitary manner.

### 2.2 Subsystem Partitioning: Inside vs. Outside

To track information flow, we partition the total Hilbert space into:
\[
\mathcal{H} \;=\; \mathcal{H}_{\text{inside}} \,\otimes\, \mathcal{H}_{\text{outside}}.
\]
- **Outside**: The region accessible to distant observers, emitting Hawking radiation that eventually escapes to infinity.  
- **Inside**: The structured, non-singular core region plus any matter or negative-energy modes that remain behind the horizon.

A unitarity-respecting scenario must **preserve** the purity of the overall state \(\lvert \Psi\rangle_{\text{total}}\in\mathcal{H}\) even if the outside “looks” thermal for practical timescales.

---

## 3. Toy Model Approaches

Below are **two** partial frameworks for how one might see quantum information eventually leave the black hole or remain accessible in a globally pure state.

### 3.1 Page Curve and Entanglement Islands

1. **Page Curve**: In standard unitarity arguments for evaporating black holes, the **entanglement entropy** of the external radiation initially rises, but must eventually **turn over** and decrease back to zero as the black hole approaches complete evaporation. This yields the “Page curve” behavior, a hallmark of unitary evaporation.  
2. **Islands Mechanism (AdS/CFT)**: Recent developments in holographic setups (AdS/CFT, quantum extremal surfaces) suggest that a portion of the black hole interior (the “island”) is effectively encoded in the outside radiation’s degrees of freedom.  
   - Even though our scenario might not be strictly AdS/CFT, the concept is that as more and more radiation leaks out, the interior degrees of freedom become entangled in such a way that the **outside** mode set can reconstruct or “encode” large swathes of the interior.  
   - In principle, the final state seen by an asymptotic observer is pure, matching standard quantum mechanics.

**Partial Application to Our Non-Singular Core**  
- We assume that the core’s structure plus quantum gravitational corrections inside the horizon allow for an “island” region that effectively merges with the outside radiation’s Hilbert space at late times.  
- The net result is that the black hole never forms a strict singularity, and the interior degrees of freedom become “decoded” or “absorbed” by the external sector as evaporation proceeds.

### 3.2 Complementarity / Firewall vs. Non-Singular Core

Historically, **black hole complementarity** posits that observers outside see a “membrane” at the horizon that reprocesses information, while an infalling observer sees no drama at the horizon—leading to the puzzle of “firewalls” if one tries to forcibly combine frames. However, in a **non-singular interior** approach:

- The “firewall” would be replaced by a finite-curvature region controlling negative-energy flux and storing quantum states.  
- The core still must “transfer” or “hand off” information to the outside radiation, presumably through a quantum channel that couples interior modes to the horizon-scale modes.  
- In principle, no real paradox arises if quantum gravity enforces that the “inside story” never irretrievably decouples from the outside Hilbert space.

**Partial Conclusion**: The complementarity or firewall debate might be softened by the existence of a self-regulating interior. Yet the detailed mechanism for how the horizon + core degrees of freedom remain entangled with external radiation while preserving a smooth experience for infalling observers is not fully resolved.

---

## 4. Minimal Unitary Evolution Model

We can attempt a simplified quantum circuit model to represent the black hole as a **time-evolving density matrix** \(\rho_{\text{BH}}(t)\):

1. **Initial Conditions**: The black hole is formed from a pure state \(\lvert \Psi_0\rangle\) of collapsing matter.  
2. **Discrete Time Steps**: At each small step \(\Delta t\), a portion of the black hole’s Hilbert space \(\Delta \mathcal{H}_{\text{inside}}\) transitions to **outgoing radiation** \(\Delta \mathcal{H}_{\text{rad}}\).  
3. **Unitary Coupling**: We impose a **global** unitary operator \(U_{\Delta t}\) that acts on \(\mathcal{H}_{\text{inside}} \otimes \mathcal{H}_{\text{ext}}\). Part of the black hole’s state entangles with and partially transfers to \(\mathcal{H}_{\text{outside}}\).  
4. **No Remnants**? If the black hole fully evaporates, \(\mathcal{H}_{\text{inside}}\) shrinks to zero dimension, while the outside Hilbert space \(\mathcal{H}_{\text{radiation}}\) ends up in a pure state that reconstructs all original information.  
   - Alternatively, if a stable Planck-scale core remains, the final product is a **mixed** external state plus a small “remnant,” unless we embed that “remnant” fully into the global unitarity framework.

**Key Challenge**: In a real black hole, the horizon radius shrinks, and the interior is dynamically regulated. A toy quantum circuit cannot easily incorporate local geometry changes. Yet it does demonstrate a **mechanism** for how unitarity might be upheld: repeated interactions between inside modes and newly emitted modes in a controlled quantum channel.

---

## 5. Potential Resolutions and Pitfalls

1. **Information Remains in the Core**: If the black hole does not evaporate entirely, a Planck-size or finite-size remnant might store the full quantum information. Then unitarity is not violated but is “locked” in the interior.  
2. **Information Gradually Leaks Out**: Over the black hole’s lifetime, more and more entanglement flows outward. Eventually, external radiation recovers all information, giving a pure final state.  
3. **Mixed Remnant**: Partial unitarity could remain consistent if the final outside + core ensemble is pure globally, even if the outside alone looks thermal.  

**Pitfalls**:  
- If no consistent global wavefunction is definable (due to strong quantum gravity effects), or if interior excitations are truly “lost” to a singular region, it’s unclear how to maintain unitarity.  
- Some scenarios run into the “firewall paradox,” requiring drastic changes at or near the horizon for consistent entanglement structure. A non-singular interior might evade or shift the location of this tension but does not trivially solve it.

---

## 6. Open Directions

- **Backreaction and Full Quantum Gravity**: Real solutions require an integrated approach coupling quantum fields + local emission + interior geometry changes, ensuring that \(\rho_{\text{BH}}(t)\) remains pure under the evolving metric.  
- **Island/Replica Wormhole Formalisms**: In AdS/CFT contexts, the “island” prescription can produce the Page curve. A self-regulating black hole might mimic that effect in asymptotically flat spacetimes, but we lack a strict, universally accepted formalism.  
- **Quantum Error Correction**: Some have argued the interior is effectively an error-correcting code encoding states that reappear in the outside radiation. Precisely how such a code is realized in a non-singular interior is still unclear.

---

## 7. Summary

While no consensus or definitive derivation exists, we’ve outlined partial frameworks and analogies for **how** information could flow out of a non-singular black hole interior:

- **Entanglement transfer**: The interior (core) degrees of freedom steadily become encoded in the outward Hawking (or Hawking-like) flux.  
- **Islands or complementarity**: Either via islands (in a holographic approach) or via black hole complementarity extended to non-singular interiors, one can maintain a global pure state without classical singularities.  
- **Quantum circuit**: A minimal toy model in discrete steps can demonstrate how repeated unitary “leaking” from inside to out can produce a final pure state of radiation.

**Open issues**—like backreaction, horizon-scale boundary conditions, firewall paradox, and strong quantum gravitational corrections—remain formidable. Yet, these partial pictures represent plausible ways black holes might avoid information loss if the interior is truly finite-curvature and dynamically regulated.

---

Below is a concise list of **open questions** that remain for the **partial information flow mechanism**, even after sketching how a non-singular black hole interior might preserve unitarity and transfer information outward:

---

## 1. Full Quantum Gravity and Backreaction

- **Coupled Evolution**  
  The partial approach outlines how quantum states might evolve in a slowly changing or “effectively classical” geometry. In reality, strong quantum gravitational effects near the core or horizon could alter the spacetime significantly. A fully self-consistent treatment must solve the metric dynamics and quantum field equations together.

- **Planckian Unknowns**  
  At extremely high curvature or near the Planck scale, standard semiclassical tools may fail. Precisely how information is stored and released in this regime remains beyond current theoretical frameworks.

---

## 2. Observer and Frame Dependence

- **Complementarity vs. Global Description**  
  Black hole complementarity suggests that different observers (outside vs. infalling) see different “accounts” of horizon physics. A globally consistent, unitary evolution might require reconciling apparently contradictory pictures without leading to paradoxes like firewalls.

- **Interior vs. Exterior Hilbert Spaces**  
  The partial model divides the total Hilbert space into \(\mathcal{H}_{\text{inside}} \otimes \mathcal{H}_{\text{outside}}\). But the precise definition of “inside” states can depend on slicing or gauge choices, complicating claims of unitarity in a truly global sense.

---

## 3. Mechanism of Information Transfer

- **How Exactly Does the Core Output Information?**  
  Even if local or horizon-scale Hawking-like flux is entangled with the core, the physical channel by which internal states become encoded in outgoing modes is not fully spelled out. One still needs a deeper explanation of negative-energy partners, horizon boundary conditions, and entanglement structure.

- **State-Dependent vs. Universal Mechanisms**  
  If the black hole interior encodes a wide variety of initial states, does the same local emission process guarantee retrieval of all possible microstates? Or does the system rely on intricate “quantum error correction” that’s still poorly understood?

---

## 4. Late-Stages and Final Outcome

- **Complete Evaporation vs. Remnant**  
  A partial toy model can describe how information gradually leaks out, but if a Planck-scale (or finite-size) core remains, the final state might be a mixed ensemble unless one proves that remaining degrees of freedom don’t lock away essential quantum data.

- **Page Curve Realization**  
  Standard unitarity arguments require the black hole’s entanglement entropy to return to zero by the end of evaporation. Does a non-singular interior replicate the same Page curve behavior or produce novel deviations, especially near the final mass scale?

---

## 5. Compatibility With Other Approaches (Islands, AdS/CFT, etc.)

- **Extension to Asymptotically Flat Spacetimes**  
  Much progress on the information paradox has come from AdS/CFT (holography), where “islands” and quantum extremal surfaces can yield the Page curve. It remains unclear whether these methods map directly onto physically realistic, asymptotically flat black hole scenarios.

- **Non-Holographic Frameworks**  
  If the interior is non-singular in a purely four-dimensional, non-holographic model, what replaces the role of boundary conformal field theories or quantum extremal surfaces? This gap requires a new or generalized theoretical toolset.

---

## 6. Experimental or Observational Tests

- **Detectability**  
  If information does eventually escape, do we see any imprint on the outgoing Hawking flux that differs from a purely thermal signature in realistic astrophysical observations? The tiny difference from pure thermality may be extremely hard to detect.

- **Quantum Signatures**  
  Confirming unitarity demands measuring subtle correlations in the black hole’s emitted radiation—likely far beyond current technology. No clear path exists for verifying these quantum correlations observationally at macroscopic distances.

---

## 7. Internal Consistency and Firewalls

- **Smooth Horizon vs. Firewalls**  
  In many unitarity-preserving scenarios, there is tension with the equivalence principle: if late-time radiation is highly entangled with the earlier flux, some arguments say an infalling observer must encounter a “firewall.” A self-regulating core might shift the location or existence of the firewall, but details remain unsettled.

- **Fate of Infalling Observers**  
  Does an observer falling into a non-singular interior see a smooth transition all the way to the core, or do quantum effects abruptly alter the experience near a certain radius? None of the partial pictures fully clarifies the infalling observer’s perspective while still ensuring global unitarity.

---

### Summary

While the **partial information flow mechanism** proposes how a finite-curvature interior and careful handling of quantum states could preserve unitarity, many open issues persist:

1. Fully **coupling** quantum fields to a dynamically evolving geometry at high curvature.  
2. Deciding the **observer-dependent** horizon structure and the true global Hilbert space.  
3. Specifying a **microscopic** channel for how states inside the core become entangled with or transferred to outgoing modes.  
4. Clarifying whether **final evaporation** or stable remnants store or release information.  
5. Connecting to established formalisms (e.g., **island prescriptions**) in realistic, non-holographic settings.  
6. **Observational** prospects for verifying or falsifying these scenarios.  
7. Ensuring a **smooth interior** for infalling observers without violating entanglement constraints.

Solving these challenges likely requires a deeper framework that unifies quantum gravity, semiclassical radiation dynamics, and the principle of no singularities.