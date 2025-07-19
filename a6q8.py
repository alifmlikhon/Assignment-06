import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Given data
S0 = 32  # Stock price
K_bull_lower = 25  # Lower strike for bull spread
K_bull_upper = 30  # Upper strike for bull spread
K_bear_lower = 25  # Lower strike for bear spread
K_bear_upper = 30  # Upper strike for bear spread
r = 0.05  # Risk-free rate (5% per annum)
T = 6 / 12  # Time to maturity (6 months)
volatility = 0.30  # Volatility (30%)

# Black-Scholes Formula for option price
def black_scholes_call(S, K, r, T, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

# Calculate the cost of bull spread (long call with lower strike and short call with upper strike)
bull_spread_price = black_scholes_call(S0, K_bull_lower, r, T, volatility) - black_scholes_call(S0, K_bull_upper, r, T, volatility)

# Calculate the cost of bear spread (short put with lower strike and long put with upper strike)
bear_spread_price = black_scholes_call(S0, K_bear_upper, r, T, volatility) - black_scholes_call(S0, K_bear_lower, r, T, volatility)

# Output the results
print(f"Bull Spread Cost: ${bull_spread_price:.2f}")
print(f"Bear Spread Cost: ${bear_spread_price:.2f}")