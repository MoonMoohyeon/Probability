import math
import random
import matplotlib.pyplot as plt


n = 100
p = 0.5
k = 10000


def draw_samples(n, p, k):
    samples = [0] * k
    for i in range(k):
        count = 0
        for j in range(n):
            if random.random() < p:
                count += 1
        samples[i] = count
    return samples


def binomial_pmf(n, p):
    pmf = [0] * (n + 1)
    for k in range(n + 1):
        pmf[k] = math.comb(n, k) * p**k * (1 - p) ** (n - k)
    return pmf


def binomial_cdf(n, p):
    cdf = [0] * (n + 1)
    cdf[0] = binomial_pmf(n, p)[0]
    for k in range(1, n + 1):
        cdf[k] = cdf[k - 1] + binomial_pmf(n, p)[k]
    return cdf


def plot_histogram(samples):
    plt.hist(samples, bins=max(samples) - min(samples) + 1, density=True)
    plt.title("Histogram of Samples")
    plt.xlabel("Count")
    plt.ylabel("Frequency")
    plt.show()


def plot_empirical_cdf(samples):
    n = len(samples)
    x = sorted(samples)
    y = [(i + 1) / n for i in range(n)]
    plt.plot(x, y, marker=".", linestyle="none")
    plt.title("Empirical CDF of Samples")
    plt.xlabel("Count")
    plt.ylabel("Cumulative Probability")
    plt.show()


samples = draw_samples(n, p, k)
pmf = binomial_pmf(n, p)
cdf = binomial_cdf(n, p)

plot_histogram(samples)
plot_empirical_cdf(samples)

plt.stem(range(n + 1), pmf, use_line_collection=True)
plt.title("PMF of Binomial RV")
plt.xlabel("Count")
plt.ylabel("Probability")
plt.show()

plt.step(range(n + 1), cdf)
plt.title("CDF of Binomial RV")
plt.xlabel("Count")
plt.ylabel("Cumulative Probability")
plt.show()
