
import numpy as np
import pandas as pd
import os

def simulate_ab_test(n_A=10000, n_B=10000, p_A=0.11, p_B=0.13, output_path='data/simulated_ab_test.csv'):
    """Simulates an A/B test and saves the dataset as a CSV file."""

    np.random.seed(42)  # For reproducibility

    # Simulate conversions
    group_A = np.random.binomial(n=1, p=p_A, size=n_A)
    group_B = np.random.binomial(n=1, p=p_B, size=n_B)

    # Combine into a DataFrame
    df = pd.DataFrame({
        'group': ['A'] * n_A + ['B'] * n_B,
        'converted': np.concatenate([group_A, group_B])
    })

    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save to CSV
    df.to_csv(output_path, index=False)
    print(f"Simulated A/B test data saved to {output_path}")

if __name__ == '__main__':
    simulate_ab_test()
