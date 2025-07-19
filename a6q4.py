import numpy as np

# Given parameters
S0 = 40  # Stock price
r = 0.10  # Risk-free rate (continuously compounded)
T = 1  # Time to maturity (1 year)

# (a) Calculate the forward price using the formula: F = S0 * exp(r * T)
F = S0 * np.exp(r * T)

# (b) Initial value of the forward contract is always zero at initiation
initial_value = 0

# Output the results
print(f"(a) Forward Price: ${F:.2f}")
print(f"(b) Initial Value of the Forward Contract: ${initial_value:.2f}")

# Now, 6 months later:
S_t = 45  # New stock price after 6 months
r = 0.10  # Risk-free rate remains the same

# Calculate the new forward price at 6 months for the remaining 6 months to maturity
F_t = S_t * np.exp(r * (T - 0.5))  # The remaining time to maturity is 0.5 years

# (b) Value of the forward contract at 6 months
forward_value = S_t - F_t  # Value of the forward contract is the difference between stock