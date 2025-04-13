import random
import math
import matplotlib.pyplot as plt

# Set parameters
lambd = 2
n = [10, 100, 1000, 10000]


def inverse_exponential_cdf(u, lambd):
    return -1 / lambd * math.log(1 - u)


def generate_exponential(lambd):
    u = random.uniform(0, 1)  # Generate random number from [0, 1]
    x = inverse_exponential_cdf(u, lambd)
    return x


for num in n:
    # Generate samples and calculate empirical CDF
    samples = []
    for i in range(num):
        samples.append(generate_exponential(lambd))
    samples.sort()
    y = [i / num for i in range(1, num + 1)]

    # Plot empirical CDF and compare with the exponential CDF
    fig, ax = plt.subplots()
    ax.plot(samples, y, label="Empirical CDF")
    ax.plot(
        samples, [1 - math.exp(-lambd * x) for x in samples], label="Exponential CDF"
    )
    ax.set_xlabel("x")
    ax.set_ylabel("F(x)")
    ax.legend()
    plt.title(f"Empirical CDF for n = {num}")
    plt.show()
