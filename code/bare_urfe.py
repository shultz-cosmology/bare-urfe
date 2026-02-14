import numpy as np
import scipy.linalg

def run_coherent_torus_urfe(L=8, iterations=20000, beta=4.0):
    N = L**2
    psi = (np.random.randn(N, N) + 1j * np.random.randn(N, N)) * 0.5
    
    # Torus Vacuum
    v = np.zeros(N)
    v[0], v[1], v[-1] = 1.0, 0.1, 0.1
    omega_0 = scipy.linalg.circulant(v) * 0.35
    
    print(f"Executing Coherent Torus Run: β={beta}, Filtering=Active")

    for n in range(iterations):
        delta_op = psi @ psi.conj().T + 1e-7 * np.eye(N)
        eigenvalues, eigenvectors = np.linalg.eigh(delta_op)
        
        # COHERENCE FILTER: Zero out eigenvalues below the 5% energy threshold
        # This focuses the 4D flow into the 'Physical' 3D modes
        total_energy = np.sum(eigenvalues)
        threshold = 0.05 * total_energy
        filtered_eigs = np.where(eigenvalues > threshold, eigenvalues, 0)
        
        # Reconstruct filtered Generator
        log_delta = eigenvectors @ np.diag(np.log(np.maximum(filtered_eigs, 1e-10))) @ eigenvectors.conj().T
        modular_flow = scipy.linalg.expm(1j * beta * (1j * log_delta))
        
        # Harmonic Analysis for Feedback
        eigs_sorted = np.sort(np.real(filtered_eigs))[::-1]
        harmonic_sum = np.sum(eigs_sorted[:3]) / (np.sum(eigs_sorted) + 1e-10)
        
        # Interaction (Evolved)
        epsilon = 0.25 + (harmonic_sum * 0.1)
        psi_next = modular_flow @ psi + omega_0 + (epsilon * (psi @ psi @ psi))
        
        # Normalization
        norm = np.sqrt(np.real(np.trace(psi_next.conj().T @ psi_next)))
        psi = psi_next / norm
        
        if n % 2500 == 0 or n == iterations - 1:
            sigma8 = harmonic_sum * 0.75 
            print(f"Iter {n:5d} | Harmonic Σ: {harmonic_sum:.4f} | σ8 Composite: {sigma8:.5f}")

    return sigma8

if __name__ == "__main__":
    run_coherent_torus_urfe()
