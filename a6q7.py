import numpy as np
from scipy.stats import norm

# Given data
S = 19  # Stock price
K = 20  # Strike price
r = 0.03  # Risk-free rate (3% per annum)
T = 4 / 12  # Time to maturity (4 months)
call_price = 1  # European call option price

# Calculate d1 and d2 using the Black-Scholes formula
d1 = (np.log(S / K) + (r + 0.5 * 0.3**2) * T) / (0.3 * np.sqrt(T))  # Assuming volatility = 30%
d2 = d1 - 0.3 * np.sqrt(T)

# Price of the European put option using put-call parity
put_price = call_price + K * np.exp(-r * T) - S

# Output the put option price
print(f"Price of the European Put Option: ${put_price:.2f}")