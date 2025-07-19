The popular explanation of Hawking radiation using particle-antiparticle pairs is a simplified analogy that Hawking himself used, but it's not entirely accurate and can lead to misconceptions about symmetry. In reality, the process isn't symmetric in the way you might expect (with equal chances of particles or antiparticles falling in), and it doesn't rely on literal virtual pairs popping into existence and splitting at the horizon. Instead, it's a quantum field theory (QFT) effect in curved spacetime, where the definition of "particles" and "vacuum" differs for observers at different locations, leading to a net outflow of positive-energy radiation (consisting of both particles and antiparticles equally) and a corresponding negative-energy influx into the black hole, causing mass loss.

I'll explain this step by step, starting with why the analogy is misleading, then diving into the actual mechanism, and finally presenting the key mathematics from Hawking's derivation (using Bogoliubov transformations). This shows why there's no equal probability of "positive particles falling in" to cancel the effect—the geometry of the black hole enforces an asymmetry.

### 1. The Popular Analogy and Why It Seems Symmetric (But Isn't)
The heuristic you described comes from Hawking's own popular writings (e.g., in *A Brief History of Time*): Quantum vacuum fluctuations constantly produce virtual particle-antiparticle pairs everywhere in space, even near a black hole's event horizon. Normally, these pairs annihilate almost immediately, but near the horizon, tidal forces from gravity can separate them before annihilation. If one crosses the horizon (falling in) while the other escapes, the escaping one becomes "real" and carries away energy, and the black hole loses mass equivalent to that energy (via \(E = mc^2\)).

Your question: Why don't particles fall in just as often as antiparticles, with antiparticles escaping? If that happened equally, there'd be no net mass loss—the black hole would gain mass from infalling positive-energy particles as often as it loses from infalling "negative" antiparticles.

The issue is that this analogy is oversimplified and misleading:
- **Particles and antiparticles both have positive mass and energy.** Antiparticles aren't "negative energy" in any intrinsic way; that's a myth from old interpretations of Dirac's equation. In modern QFT, both have positive energy, and the radiation emitted includes equal numbers of particles and antiparticles (since it's thermal radiation). [2](https://www.reddit.com/r/askscience/comments/305dtq/why_does_hawking_radiation_not_have_an_equal/), [0](https://astronomy.stackexchange.com/questions/2221/black-hole-hawking-radiation-why-only-capture-anti-particle)

- **The "antiparticle falls in" part is just a storytelling device.** Hawking used it to make the idea intuitive, but he later clarified it's not literal. The real process doesn't involve preferential capture of antiparticles; instead, it's about how the black hole's curvature distorts the quantum vacuum, creating real particles from "nothing" at the expense of the black hole's gravitational energy. [18](https://www.quora.com/How-did-the-common-misconception-of-the-origin-of-Hawking-radiation-due-to-particle-antiparticle-pairs-at-the-Schwarzschild-surface-become-so-pervasive-if-it-is-so-wrong-Why-would-Hawking-himself-even-mention-it-in), [4](https://bigthink.com/starts-with-a-bang/hawking-radiation-black-hole-evaporation/)
- **No true symmetry in outcomes.** The horizon acts like a one-way membrane: From the perspective of a distant observer, the escaping radiation is always positive-energy (reducing the black hole's mass), and the infalling part is effectively negative-energy (a deficit in the vacuum). This asymmetry comes from the spacetime geometry—the event horizon separates regions where energy definitions differ. [25](https://en.wikipedia.org/wiki/Hawking_radiation)

In short, the analogy suggests randomness (50/50 chance), but the actual math shows a biased, thermal process where net positive energy always escapes.

### 2. The Actual Mechanism: Quantum Fields in Curved Spacetime
Hawking radiation arises from applying QFT to the curved spacetime around a black hole (formed by gravitational collapse). Key insights:
- **Different vacuums for different observers.** In flat space, everyone agrees on what "vacuum" (no particles) means. But in curved space near a black hole, the vacuum for an observer far away (at infinity) looks like a sea of particles to someone near the horizon (similar to the Unruh effect for accelerating observers). [25](https://en.wikipedia.org/wiki/Hawking_radiation)
The distant observer sees outgoing radiation because the black hole's formation "excites" the vacuum.
- **Negative energy influx.** The escaping positive-energy particles are correlated with negative-energy "partners" that fall into the black hole. Negative energy is allowed inside the horizon (where the time-like Killing vector becomes space-like), violating classical energy conditions but permitted quantumly. This reduces the black hole's mass without needing "negative mass" antiparticles. [26](https://arxiv.org/pdf/2502.13026), [8](https://math.ucr.edu/home/baez/physics/Relativity/BlackHoles/hawking.html)
- **Why no equal positive infall?** The process isn't probabilistic in the classical sense; it's determined by the mode propagation in spacetime. During collapse, incoming vacuum modes (from past infinity) get "scrambled" by the horizon: outgoing modes at future infinity contain particles, while infalling modes have a negative-energy correlation to conserve total energy. There's no mechanism for equal positive-energy infall because the horizon geometry biases the flux—positive energy propagates outward, negative inward. [26](https://arxiv.org/pdf/2502.13026) The radiation is thermal (blackbody-like), so it includes particles and antiparticles symmetrically in the outflow, but the net effect is always mass loss.

This resolves the information paradox debates too, but that's beyond your question.

### 3. The Math: Derivation Using Bogoliubov Transformations
Hawking's 1975 paper derives this rigorously for a collapsing star forming a black hole. [25](https://en.wikipedia.org/wiki/Hawking_radiation) The key tool is Bogoliubov transformations, which relate quantum field modes before ("in" modes at past null infinity, \(I^-\)) and after ("out" modes at future null infinity, \(I^+\)) the collapse. These show how the initial vacuum state evolves into a state with particles.

Consider a massless scalar field (for simplicity; it generalizes to other fields). The field is expanded in modes:
- In modes: \(\phi_{\text{in}_i}\) (positive frequency w.r.t. affine parameter at \(I^-\)).
- Out modes: \(\phi_{\text{out}_j}\) (positive frequency at \(I^+\)).

The transformation is:

\phi_{\text{out}_j} = \sum_i \left( \alpha_{ji} \phi_{\text{in}_i} + \beta_{ji} \phi_{\text{in}_i}^* \right),

where \(\alpha_{ji}\) and \(\beta_{ji}\) are Bogoliubov coefficients (complex numbers). The \(\beta\) terms mix creation and annihilation operators, leading to particle creation.

The annihilation operator for in modes is:

a_{\text{in}_i} = \sum_j \left( \alpha_{ji} a_{\text{out}_j} + \beta_{ji}^* a_{\text{out}_j}^\dagger \right).


If the system starts in the in-vacuum (\(a_{\text{in}_i} | \text{in} \rangle = 0\)), the number of particles in out modes is:

\langle \text{in} | N_{\text{out}_j} | \text{in} \rangle = \sum_i |\beta_{ji}|^2,

where \(N_{\text{out}_j} = a_{\text{out}_j}^\dagger a_{\text{out}_j}\). If \(\beta = 0\), no particles; but for black holes, \(\beta \neq 0\) due to the time-dependent metric during collapse.

To compute \(\beta\), use wave packets for late-time emissions (focusing on radiation after horizon formation). For Schwarzschild black holes (mass \(M\)), the relation is:

|\alpha_{j \omega'}| = e^{4\pi M \omega_j} |\beta_{j \omega'}|,

leading to the normalization (for bosons):

\int_0^\infty d\omega' \left( |\alpha_{j \omega'}|^2 - |\beta_{j \omega'}|^2 \right) = 1.


Substituting gives the thermal spectrum:

\int_0^\infty d\omega' |\beta_{j \omega'}|^2 = \frac{1}{e^{8\pi M \omega_j} - 1},

which is a Planck distribution at Hawking temperature \(T_H = \frac{1}{8\pi M}\) (in units where \(\hbar = c = G = k_B = 1\); in full units, \(T_H = \frac{\hbar c^3}{8\pi G M k_B}\)).

**Why asymmetry and mass loss?** The \(\beta\) terms create particle-antiparticle pairs from the vacuum, but the geometry ensures positive-energy modes propagate to \(I^+\) (escaping as radiation), while negative-frequency components (effective negative energy) are trapped or fall in near the horizon. This is because inside the horizon, negative energy is stable (Killing vector flips). The total energy is conserved globally: positive energy out = negative energy in, reducing \(M\). For fermions, it's similar but with Fermi-Dirac statistics (\(+1\) in denominator). [26](https://arxiv.org/pdf/2502.13026), [19](https://www.desy.de/user/projects/Physics/Relativity/BlackHoles/hawking.html)

Particles and antiparticles appear equally in the radiation (thermal equilibrium), but there's no "equal opposite" infall of positive energy because the Bogoliubov mixing is biased by the horizon—the calculation yields net positive flux out.
