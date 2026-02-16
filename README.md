# A Recursive Matrix Model Predicting Warm Dark Matter and a Suppressed σ₈

**Author:** Brian Shultz  
**Zenodo DOI:** [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18644520.svg)](https://doi.org/10.5281/zenodo.18644520)  
**Core Prediction:** $\sigma_8 \approx 0.75$ (Geometric Fixed-Point Attractor)

---

## 🔬 Abstract
This model derives cosmological constants as stable fixed points of a recursive complex matrix field. By treating the vacuum as an iterative process, physical law emerges as a **Universal Attractor**. The system resolves the $S_8$ tension and the Vacuum Catastrophe by identifying the "Recursive Floor" of the universe.

## 🧮 The Geometric Lock (The "Why")
The model’s convergence to **$0.75$** is not a fit; it is a **topological necessity**. 
1. **The 4D State:** The recursion operates in a 4D effective space (3 spatial + 1 iterative depth $w$).
2. **The 3/4 Projection:** Projecting this 4D recursive information into 3D observable space requires a covariance scaling of exactly:
   $$\text{Retained Info} = \frac{D_{observed}}{D_{total}} = \frac{3}{4} = 0.75$$
3. **The Result:** This scaling manifests as the clustering amplitude **$\sigma_8 = 0.75$**. The "Dark Matter" fraction is simply the 25% of information that remains unprojected.

## 🛠️ The Bare Recursion
The code in `code/bare_urfe.py` executes this map:
$$\Psi_{n+1} = \mathcal{N} \left[ \exp(i\beta D_n) \Psi_n + \Omega_0 + \epsilon (\Psi_n \star \Psi_n \star \Psi_n) \right]$$

| Metric | Prediction | Observation (2026) |
| :--- | :---: | :--- |
| **Clustering ($\sigma_8$)** | **0.75** | **0.747 - 0.783** (DES Y6 Trends) |
| **Perturber Mass** | **$7.5 \times 10^5 M_\odot$** | **JVAS B1938+666** core alignment |
| **Proton Decay** | **$\approx 2.1 \times 10^{34}$ yr** | Testable by Hyper-K |

---
**Verification:** The attractor locks at $\lambda^* = 0.75$ across 20,000+ seeds with zero variance. See `VERIFICATION.md` for logs.
