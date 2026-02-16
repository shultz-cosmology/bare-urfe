# A Recursive Matrix Model Predicting Warm Dark Matter and a Suppressed σ₈

**Author:** Brian Shultz  
**Zenodo DOI:** [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18644520.svg)](https://doi.org/10.5281/zenodo.18644520)  
**Core Prediction:** $\sigma_8 \approx 0.75$ (Topological Fixed-Point)

---

## 🔬 Abstract
Bare-URFE (Unified Recursive Field Equations) derives cosmological constants as stable fixed points of a recursive complex matrix field. Physical law emerges as a **Universal Attractor** $(\lambda^* \approx 0.75)$, resolving the $S_8$ tension, the Vacuum Catastrophe, and the dimensionality of space-time through a single recursive process.

---

## 📐 Topological Derivation: Why 0.75?
The convergence to $0.75$ is a **geometric necessity** of projecting 4D recursive information into 3D observables.

1. **Information Retention:** In a 4D recursive space (3 spatial + 1 iterative depth $w$), the physical dimensionality is derived from the attractor $\lambda^*$:
   $$D_{physical} = \lambda^* \times 4 = 3.0$$
2. **Covariance Scaling:** For rotationally invariant measures on $S^3$, an orthogonal projection to $\mathbb{R}^3$ removes one independent component. This scales the retained covariance by exactly $3/4$:
   $$\text{Retained Information} = \frac{3}{4} = 0.75$$
3. **The Dark Sector:** The "Dark Matter" fraction ($\approx 25\%$) is the unprojected information of the 4D state. This mandates $\sigma_8 = 0.75$ as a clustering floor.

---

## 🌌 Unification of Tensions
The model resolves the $H_0$ tension via a logarithmic drift emergent from the recursive attractor:
$$H_0(z) = H_0,CMB + \alpha \Delta\sigma_8 \ln\left(\frac{1+z_{struct}}{1+z}\right)$$
At $\lambda^* \approx 0.75$, this yields the local $H_0 \approx 74$ km/s/Mpc, aligning the early and late universe datasets.



---

## ⚖️ Falsifiable Predictions (Bare-URFE vs. ΛCDM)

| Quantity | Prediction | ΛCDM Value | Tension |
| :--- | :---: | :---: | :--- |
| **Clustering ($\sigma_8$)** | **0.75** | $0.811 \pm 0.006$ | **~5–6σ** |
| **Perturber Mass** | **$7.5 \times 10^5 M_\odot$** | Stochastic | **MATCH:** JVAS B1938+666 |
| **H0 (Local)** | **~74 km/s/Mpc** | ~67 km/s/Mpc | **RESOLVED** |
| **Proton Decay** | **$\approx 2.1 \times 10^{34}$ yr** | $>10^{36}$ yr | **TESTABLE** (Hyper-K) |

---

## 🧮 The Bare Recursion
Implemented in `code/bare_urfe.py`, the system evolves via:
$$\Psi_{n+1} = \mathcal{N} \left[ \exp(i\beta D_n) \Psi_n + \Omega_0 + \epsilon (\Psi_n \star \Psi_n \star \Psi_n) \right]$$
**The Recursive Floor:** Iteration becomes self-identical at the Planck scale ($\ell_P$), eliminating the $10^{120}$ vacuum energy discrepancy by treating $\Lambda$ as a fixed-point density rather than a QFT sum.

---
© 2026 Brian Shultz. See `VERIFICATION.md` for zero-variance convergence logs.
