import numpy as np
import matplotlib.pyplot as plt

# Given data
S = np.linspace(30, 60, 100)  # Asset price range from $30 to $60
K_call = 45  # Call option strike price
K_put = 40  # Put option strike price
call_premium = 3  # Cost of the call option
put_premium = 4  # Cost of the put option

# Long call payoff: max(0, S - K_call) - Call Premium
call_payoff = np.maximum(0, S - K_call) - call_premium

# Long put payoff: max(0, K_put - S) - Put Premium
put_payoff = np.maximum(0, K_put - S) - put_premium

# Total profit = Call Profit + Put Profit
total_profit = call_payoff + put_payoff

# Plot the Profit Diagram
plt.figure(figsize=(8, 5))

# Plot profit for combination of options
plt.plot(S, total_profit, label="Total Profit (Call + Put)", color="blue", linewidth=2)

# Labels and title
plt.title('Profit and Payoff Diagram for Combination of Call and Put')
plt.xlabel('Asset Price at Expiration ($)')
plt.ylabel('Profit ($)')
plt.axhline(0, color='black',linewidth=1)  # Horizontal line for 0 profit
plt.axvline(K_call, color='red', linestyle='--', label="Strike Price (Call)")
plt.axvline(K_put, color='green', linestyle='--', label="Strike Price (Put)")
plt.legend(loc='best')
plt.grid(True)
plt.show()