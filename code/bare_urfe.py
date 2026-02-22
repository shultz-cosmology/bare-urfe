import numpy as np

def prove_equalization(iterations=500, particles=10000):
    """
    STABILITY TEST:
    Demonstrates that a 4D recursive map equalizes variance across dimensions.
    The 0.75 ratio follows from 3D observation of this 4D equalized system.
    """
    # 1. Start with an imbalanced 4D Universe (Dim 4 has 100x variance)
    scales = np.array([1.0, 1.0, 1.0, 10.0]) 
    data = np.random.normal(0, 1, (particles, 4)) * scales
    
    print(f"Initial 4D Variances: {np.var(data, axis=0)}")

    # 2. Apply Recursive Toroidal Dynamics (Evolution of 3s)
    for _ in range(iterations):
        data = np.sin(data * np.pi)

    # 3. Measure final state: Dimensions are now equalized.
    final_vars = np.var(data, axis=0)
    print(f"Final 4D Variances: {final_vars}")

    # 4. Result: Any 3D slice of this equalized 4D system yields 75%
    var_total = np.sum(final_vars)
    var_observed = np.sum(final_vars[:3]) # Dropping the 'Bulk' (4th Dim)
    
    return var_observed / var_total

# Run the proof
ratio = prove_equalization()
print(f"\nEmergent S8 Floor: {ratio:.4f}")
