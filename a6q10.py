import numpy as np

# Given data
S0 = 60  # Futures price
K = 60   # Strike price
r = 0.08  # Risk-free rate (8% per annum)
T = 6 / 12  # Time to maturity (6 months)
volatility = 0.30  # Volatility (30%)
steps = 2  # Number of steps in the binomial tree

# Time step
dt = T / steps

# Up and down factors
u = np.exp(volatility * np.sqrt(dt))  # Up factor
d = 1 / u  # Down factor

# Risk-neutral probability
p = (np.exp(r * dt) - d) / (u - d)

# Option payoff at final nodes
payoff_up = max(S0 * u - K, 0)
payoff_down = max(S0 * d - K, 0)

# Discount the payoffs to present value
option_value = (p * payoff_up + (1 - p) * payoff_down) * np.exp(-r * dt)

# Output the result
print(f"Value of the European Call Option on Futures: ${option_value:.2f}")