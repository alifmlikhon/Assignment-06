import numpy as np

# Given data
S0 = 484  # Stock index level
K = 480  # Exercise price
r = 0.10  # Risk-free rate (10% per annum)
T = 2 / 12  # Time to maturity (2 months)
dividend_yield = 0.03  # Dividend yield (3% per annum)
volatility = 0.25  # Volatility (25% per annum)
steps = 4  # Divide the option life into 4 half-month periods
dt = T / steps  # Time step per period
u = np.exp(volatility * np.sqrt(dt))  # Up factor
d = 1 / u  # Down factor
p = (np.exp((r - dividend_yield) * dt) - d) / (u - d)  # Risk-neutral probability

# Initialize asset price tree
asset_prices = np.zeros((steps + 1, steps + 1))

# Generate the asset price tree
for i in range(steps + 1):
    for j in range(i + 1):
        asset_prices[j, i] = S0 * (u*(i - j)) * (d*j)

# Option values at final nodes (payoff)
option_values = np.maximum(K - asset_prices[:, steps], 0)

# Backtrack through the tree
for i in range(steps - 1, -1, -1):
    for j in range(i + 1):
        # American option can be exercised at each node
        option_values[j] = np.maximum(K - asset_prices[j, i], np.exp(-r * dt) * (p * option_values[j] + (1 - p) * option_values[j + 1]))

# Output the result
print(f"Value of the American Put Option: ${option_values[0]:.2f}")