import numpy as np

# Given data for the payments
payments = [460, 235, 640, 370, 330, 250]  # Payments in each year
interest_rate = 0.045  # Annual interest rate compounded quarterly
quarters_per_year = 4  # 4 quarters in a year

# Convert the annual interest rate to a quarterly rate
quarterly_rate = interest_rate / quarters_per_year

# Function to calculate present value with quarterly compounding
def present_value_quarterly(payments, quarterly_rate):
    total_pv = 0
    for t, payment in enumerate(payments, start=1):
        # Convert years to quarters
        total_pv += payment / (1 + quarterly_rate) ** (quarters_per_year * t)  # Apply discounting for each payment
    return total_pv

# Calculate the present value of the payments
pv = present_value_quarterly(payments, quarterly_rate)

# Output the result
print(f"Present Value of the investments: ${pv:.2f}")