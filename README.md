# A Recursive Matrix Model Predicting Warm Dark Matter and a Suppressed σ₈

**Author:** Brian Shultz  
**Status:** Preprint manuscript in preparation for submission.  
**Core Prediction:** σ₈ ≈ 0.75 (falsifiable by Euclid/Rubin/Lyman-α forest data).

## 📄 Manuscript
The current draft of the paper is available here: [manuscript/main.pdf](manuscript/main.pdf)

### Abstract
We present a recursive dynamical system on high-dimensional complex matrix spaces that converges to stable fixed points under minimal normalization constraints. Without any enforcement of agreement with observed physics, the system produces a universe-like attractor that deviates in specific, testable ways from ΛCDM and the Standard Model. In particular, it generically predicts a warmer sterile-neutrino dark matter sector, suppressed small-scale structure (σ₈ = 0.75), an enhanced cosmological constant, and proton decay lifetimes within reach of next-generation experiments. These deviations arise unavoidably from the bare recursion (a stripped-down version of the Unified Recursive Feedback Equation, URFE, without phenomenological "Truth Filters" that previously enforced physicality). The model is decisively falsifiable by current and near-future observations (e.g., Euclid/Rubin on σ₈). This reframes the approach as a computationally intensive, risk-bearing cosmological hypothesis comparable to lattice QCD or numerical relativity, where physical law emerges as a stable fixed point of a computational process.

## 🔬 Falsifiable Predictions
| Quantity | Bare Model Prediction | Current Observational Value | Tension |
|----------|-----------------------|-----------------------------|---------|
| σ₈       | 0.75                  | 0.811 ± 0.006 (Planck 2018) | ~5–6σ   |
| Λ        | 4.2 × 10⁻¹²¹ M_P⁴     | ~1.1 × 10⁻¹²² M_P⁴          | ~4× higher |
| m_h      | ≈ 128 GeV             | 125.10 ± 0.14 GeV           | Mild tension |
| v (EW)   | 244.7 GeV             | 246.22 GeV                  | Consistent |
| ∑m_ν     | ≈ 0.14 eV             | < 0.12 eV                   | Near bound |
| τ(p → e⁺π⁰) | ≈ 2.1 × 10³⁴ yr   | >1.6 × 10³⁴ yr              | Testable by Hyper-Kamiokande |

**Key falsifiability criterion:** This model is ruled out if upcoming surveys (Euclid, Rubin Observatory, Lyman-α forest) converge on σ₈ ≳ 0.80 with no evidence of warm dark matter suppression.

## 🧮 Model Summary
The model is defined by a recursive dynamical system on complex matrices Ψ ∈ Mat_N(ℂ):

1. **Modular operator:** Δ_Ψₙ = Ψₙ Ψₙ† + δ I  
2. **Generator:** Dₙ = i log Δ_Ψₙ  
3. **Bare recursion:**  
   Ψₙ₊₁ = exp(i β Dₙ) Ψₙ + Ω₀ + ε (Ψₙ ⋆ Ψₙ ⋆ Ψₙ)  
   followed by trace normalization.

See Section 2 of the manuscript for full details.

## 💻 Code Implementation
A runnable Python implementation of the bare URFE recursion is available in [code/bare_urfe.py](code/bare_urfe.py). The script includes:

- Full implementation of the recursion (Eq. 2.3)
- Modular operator and generator construction
- Trace normalization
- Convergence monitoring via Δρₙ

Requires `numpy` and `scipy`. Run with:
