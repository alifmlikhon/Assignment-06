import numpy as np
import matplotlib.pyplot as plt

# Given data for options
K = 150  # Strike price
premium = 5  # Premium paid for options

# Stock price range (from $100 to $200)
stock_prices = np.linspace(100, 200, 100)

# Long call option payoff: max(0, S - K) - Premium
long_call_payoff = np.maximum(0, stock_prices - K) - premium

# Short call option payoff: -max(0, S - K) + Premium
short_call_payoff = -np.maximum(0, stock_prices - K) + premium

# Long put option payoff: max(0, K - S) - Premium
long_put_payoff = np.maximum(0, K - stock_prices) - premium

# Short put option payoff: -max(0, K - S) + Premium
short_put_payoff = -np.maximum(0, K - stock_prices) + premium

# Plotting the Payoff Diagrams
plt.figure(figsize=(10, 6))

# Long Call Payoff
plt.plot(stock_prices, long_call_payoff, label="Long Call", color="blue", linestyle='-', linewidth=2)

# Short Call Payoff
plt.plot(stock_prices, short_call_payoff, label="Short Call", color="red", linestyle='--', linewidth=2)

# Long Put Payoff
plt.plot(stock_prices, long_put_payoff, label="Long Put", color="green", linestyle='-', linewidth=2)

# Short Put Payoff
plt.plot(stock_prices, short_put_payoff, label="Short Put", color="purple", linestyle='--', linewidth=2)

# Labels and title
plt.title('Payoff and Profit Diagrams for Options')
plt.xlabel('Stock Price at Expiration ($)')
plt.ylabel('Payoff ($)')
plt.legend(loc='best')
plt.grid(True)
plt.show()