import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import time

np.random.seed(int(time.time()))

# Define parameters
mu, var = 5, 25 / 3
sample_size = 10000
n_values = [1, 2, 3, 5, 10, 50]

# Generate sample values of Zn for each n
Zn_values = []
for n in n_values:
    X = np.random.uniform(0, 10, size=(sample_size, n))
    Sn = np.sum(X, axis=1)
    Zn = (Sn - n * mu) / np.sqrt(n * var)
    Zn_values.append(Zn)

# Compute and plot empirical CDF for each n
fig, axes = plt.subplots(2, 3, figsize=(10, 7))
for i, ax in enumerate(axes.flat):
    if i < len(n_values):
        n = n_values[i]
        Zn = Zn_values[i]
        x = np.sort(Zn)
        y = np.arange(1, sample_size + 1) / sample_size
        phi = norm.cdf(x)
        ax.plot(x, y, label="Empirical CDF")
        ax.plot(x, phi, label="Standard Normal CDF")
        ax.set_title("n = {}".format(n))
        ax.legend()
plt.show()
