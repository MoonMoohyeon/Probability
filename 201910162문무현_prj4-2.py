import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, expon
import time

np.random.seed(int(time.time()))

# Define parameters
lamda = 0.5
mu, var = 1 / lamda, 1 / lamda**2
sample_size = 10000
n_values = [1, 2, 3, 5, 10, 50]

# Generate sample values of Zn for each n
Zn_values = []
for n in n_values:
    X = np.random.exponential(scale=1 / lamda, size=(sample_size, n))
    Sn = np.sum(X, axis=1)
    Zn = (Sn - n * mu) / np.sqrt(n * var)
    Zn_values.append(Zn)

# Compute and plot empirical CDF for each n
fig, axes = plt.subplots(2, 3, figsize=(10, 7))
for i, ax in enumerate(axes.flat):
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
