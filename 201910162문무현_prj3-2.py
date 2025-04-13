import math
import random
import matplotlib.pyplot as plt


lambd = 1
k = 10000


def draw_samples(lambd, k):
    samples = [0] * k
    for i in range(k):
        samples[i] = -math.log(random.random()) / lambd
    return samples


def exponential_pdf(lambd, x):
    if x < 0:
        return 0
    else:
        return lambd * math.exp(-lambd * x)


def exponential_cdf(lambd, x):
    if x < 0:
        return 0
    else:
        return 1 - math.exp(-lambd * x)


def plot_histogram(samples):
    plt.hist(samples, bins="auto", density=True)
    plt.title("Histogram of Samples")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()


def plot_empirical_cdf(samples):
    n = len(samples)
    x = sorted(samples)
    y = [sum(1 for xi in samples if xi <= xi0) / n for xi0 in x]
    plt.plot(x, y, marker=".", linestyle="none")
    plt.title("Empirical CDF of Samples")
    plt.xlabel("Value")
    plt.ylabel("Cumulative Probability")
    plt.show()


samples = draw_samples(lambd, k)
pdf = [exponential_pdf(lambd, x) for x in samples]
cdf = [exponential_cdf(lambd, x) for x in samples]

plot_histogram(samples)
plot_empirical_cdf(samples)

plt.hist(samples, bins="auto", density=True)
plt.plot(samples, pdf, "r.", alpha=0.5)
plt.title("PDF of Exponential RV")
plt.xlabel("Value")
plt.ylabel("Probability")
plt.show()

x = sorted(samples)
y = [exponential_cdf(lambd, xi) for xi in x]
plt.plot(x, y)
plt.title("CDF of Exponential RV")
plt.xlabel("Value")
plt.ylabel("Cumulative Probability")
plt.show()
