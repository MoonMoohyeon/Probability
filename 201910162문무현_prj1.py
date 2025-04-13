import random
import matplotlib.pyplot as plt

# Define the range of values of n to use
n_values = [10**i for i in range(1, 7)]

# Initialize an empty list to store the estimates of π
pi_estimates = []

# Calculate the estimate of π for each value of n and store it in the pi_estimates list
for n in n_values:
    count = 0
    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if (x-0.5)**2 + (y-0.5)**2 <= 0.25:
            count += 1
    pi_hat = 4 * count / n
    pi_estimates.append(pi_hat)

# Plot the behavior of the estimator versus n
plt.plot(n_values, pi_estimates)
plt.xscale('log')
plt.xlabel('Number of samples')
plt.ylabel('Estimate of π')
plt.title('Estimating π using random sampling')
plt.axhline(y=3.14159, color='r', linestyle='-')
plt.show()
