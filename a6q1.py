import numpy as np

# Given data
cashflows_A = [225, 215, 250, 225, 205]
cashflows_B = [220, 225, 250, 250, 210]
r = 0.0433  # continuous compounding interest rate

# Calculate Present Value using continuous discounting
def present_value(cashflows, r):
    return sum(cf * np.exp(-r * t) for t, cf in enumerate(cashflows, start=1))

pv_A = present_value(cashflows_A, r)
pv_B = present_value(cashflows_B, r)

print(f"Present Value of Investment A: ${pv_A:.2f}")
print(f"Present Value of Investment B: ${pv_B:.2f}")

if pv_A > pv_B:
    print("Investment A is preferable.")
else:
    print("Investment B is preferable.")