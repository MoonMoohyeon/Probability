import random

# 201910162 문무현 prj0

# example
NUM = 1000000
K = 4
m = [0.3, 0.1, 0.4, 0.2]
res = [0, 0, 0, 0]

def func(x):
    i = 0
    tmp = m[0]
    while tmp < x and i < len(m):
        i += 1
        tmp += m[i]
    return i

# simulate * NUM
for i in range(NUM):
    ran = random.uniform(0, 1)
    rv = func(ran)
    res[rv] = res[rv] + 1

# given probabilities
for i in range(1, len(m)+1):
    print('m' + str(i) + '=' + str(m[i-1]))

# empirical PMF
for i in range(0, K):
    py = res[i] / NUM
    print('pY' + '(' + str(i+1) + ')' + '=' + str(py))

# for i in range(0, K):
#     print(res[i])
