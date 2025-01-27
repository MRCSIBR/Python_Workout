import matplotlib.pyplot as plt
import numpy as np

def compound_interest(principal, rate, time, n):
    """
    Calculate compound interest
    principal: initial investment
    rate: annual interest rate (as a decimal)
    time: time in years
    n: number of times interest is compounded per year
    """
    amount = principal * (1 + rate/n)**(n*time)
    return amount

# Set parameters
principal = 500_000  # Initial investment
rate = 0.32       # 32% annual interest rate
time = 10         # 10 years
n = 12            # Compounded monthly

# Calculate compound interest for each year
years = np.arange(0, time+1)
amounts = [compound_interest(principal, rate, t, n) for t in years]

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(years, amounts, marker='o')
plt.title('Compound Interest Over 10 Years')
plt.xlabel('Years')
plt.ylabel('Amount ($)')
plt.grid(True)

# Add annotations
plt.annotate(f'Initial: ${principal}', (0, principal), textcoords="offset points", xytext=(0,10), ha='center')
plt.annotate(f'Final: ${amounts[-1]:.2f}', (time, amounts[-1]), textcoords="offset points", xytext=(0,10), ha='center')

plt.show()

# Print the final amount
print(f"Final amount after {time} years: ${amounts[-1]:.2f}")
