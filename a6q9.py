import numpy as np
from scipy.stats import norm

# Given data
S = 30  # Stock price
K = 29  # Exercise price
r = 0.05  # Risk-free rate (5% per annum)
T = 4 / 12  # Time to maturity (4 months)
volatility = 0.25  # Volatility (25%)

# Calculate d1 and d2 using the Black-Scholes formula
d1 = (np.log(S / K) + (r + 0.5 * volatility**2) * T) / (volatility * np.sqrt(T))
d2 = d1 - volatility * np.sqrt(T)

# European Call Option Price
call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

# European Put Option Price using Put-Call Parity
put_price = call_price + K * np.exp(-r * T) - S

# Output the results
print(f"(a) European Call Option Price: ${call_price:.2f}")
print(f"(c) European Put Option Price using Put-Call Parity: ${put_price:.2f}")