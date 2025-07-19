import numpy as np

# Given parameters
face_value = 100  # assume $100 face value
coupon_rate = 0.08
yield_rate = 0.11
years = 5

# Cash flows
coupon = face_value * coupon_rate
times = np.arange(1, years + 1)
cashflows = [coupon] * (years - 1) + [coupon + face_value]

# Bond price with continuous compounding
price = sum(cf * np.exp(-yield_rate * t) for cf, t in zip(cashflows, times))

# Duration
duration = sum(t * cf * np.exp(-yield_rate * t) for cf, t in zip(cashflows, times)) / price

# Price change for 0.2% (0.002) decrease in yield
delta_y = -0.002
price_change = -duration * price * delta_y
new_price_approx = price + price_change

# Recalculate bond price at new yield 10.8%
new_yield = 0.108
new_price = sum(cf * np.exp(-new_yield * t) for cf, t in zip(cashflows, times))

# Output results
print(f"(a) Bond Price at 11% yield: ${price:.2f}")
print(f"(b) Duration: {duration:.4f} years")
print(f"(c) Price Change for -0.2% yield: ${price_change:.2f}")
print(f"    Approximated New Price: ${new_price_approx:.2f}")
print(f"(d) Recalculated Price at 10.8% yield: ${new_price:.2f}")