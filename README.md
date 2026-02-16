# A Recursive Matrix Model Predicting Warm Dark Matter and a Suppressed σ₈

**Author:** Brian Shultz  
**Zenodo DOI:** [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18644520.svg)](https://doi.org/10.5281/zenodo.18644520)  
**Status:** Preprint manuscript in preparation for submission.  
**Core Prediction:** $\sigma_8 \approx 0.75$ (Falsifiable by Euclid/Rubin/Lyman-α forest data).

---

## 🔬 Abstract
We present a recursive dynamical system on high-dimensional complex matrix spaces that converges to stable fixed points under minimal normalization constraints. Without any enforcement of agreement with observed physics, the system produces a universe-like attractor that deviates in specific, testable ways from $\Lambda$CDM and the Standard Model. 

In particular, it generically predicts a **warmer sterile-neutrino dark matter sector**, suppressed small-scale structure (**$\sigma_8 = 0.75$**), an enhanced cosmological constant, and proton decay lifetimes within reach of next-generation experiments. These deviations arise unavoidably from the **Bare Recursion**—a stripped-down version of the Unified Recursive Feedback Equation (URFE), without phenomenological "Truth Filters." The model is decisively falsifiable by current observations, reframing physical law as a stable fixed point of a computational process.

---

## ⚖️ Falsifiable Predictions (Standard Model vs. Bare-URFE)

| Quantity | Bare Model Prediction | Current Observational Value | Tension |
| :--- | :---: | :---: | :--- |
| **Clustering ($\sigma_8$)** | **0.75** | $0.811 \pm 0.006$ (Planck 2018) | **~5–6σ** |
| **Cosmo. Constant ($\Lambda$)** | $4.2 \times 10^{-121} M_P^4$ | $\sim 1.1 \times 10^{-122} M_P^4$ | ~4× higher |
| **Higgs Mass ($m_h$)** | $\approx 128$ GeV | $125.10 \pm 0.14$ GeV | Mild tension |
| **EW Vacuum ($v$)** | $244.7$ GeV | $246.22$ GeV | Consistent |
| **Neutrino Mass ($\sum m_\nu$)** | $\approx 0.14$ eV | $< 0.12$ eV | Near bound |
| **Proton Decay ($\tau$)** | $\approx 2.1 \times 10^{34}$ yr | $>1.6 \times 10^{34}$ yr | Testable (HK) |

**Key Falsifiability Criterion:** This model is ruled out if upcoming surveys (Euclid, Rubin Observatory, Lyman-α forest) converge on $\sigma_8 \gtrsim 0.80$ with no evidence of warm dark matter suppression.

---

## 🧮 Model Summary
The model is defined by a recursive dynamical system on complex matrices $\Psi \in \text{Mat}_N(\mathbb{C})$:

1. **Modular operator:** $\Delta_{\Psi_n} = \Psi_n \Psi_n^\dagger + \delta I$
2. **Generator:** $D_n = i \log \Delta_{\Psi_n}$
3. **Bare recursion:**
$$\Psi_{n+1} = \exp(i \beta D_n) \Psi_n + \Omega_0 + \epsilon (\Psi_n \star \Psi_n \star \Psi_n)$$
*Followed by trace normalization.*



---

## 💻 Code Implementation
A runnable Python implementation of the bare URFE recursion is available in `code/bare_urfe.py`. 

- **Full implementation of the recursion (Eq. 2.3)**
- **Modular operator and generator construction**
- **Convergence monitoring via $\Delta\rho_n$**

**Requirements:** `numpy`, `scipy`.  
**Usage:** `python3 code/bare_urfe.py`

---
© 2026 Brian Shultz. Published under Zenodo Archive 10.5281/zenodo.18644520.
