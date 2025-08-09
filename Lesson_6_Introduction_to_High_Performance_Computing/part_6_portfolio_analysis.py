import numpy as np

# Simulate random returns of 4 assets over 1000 time periods
returns = np.random.rand(1000, 4)

# Calculate mean return and covariance matrix
mean_return = np.mean(returns, axis=0)
covariance_matrix = np.cov(returns, rowvar=False)

# Portfolio weights
weights = np.array([0.25, 0.25, 0.25, 0.25])

# Calculate expected portfolio return
expected_return = np.dot(mean_return, weights)

print(f"Expected Portfolio Return: {expected_return}")
print(f"Covariance Matrix:\n {covariance_matrix}")
