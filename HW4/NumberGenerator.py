import numpy as np

def Normal(mean, varience):
    u = np.random.uniform(0, 1)
    v = np.random.uniform(0, 1)
    x = np.sqrt(-2 * np.log(u)) * np.cos(2 * np.pi * v)
    return x * np.sqrt(varience) + mean

def Polynomial(n, a, w):
    x = np.random.uniform(-1, 1)
    phi = [x**i for i in range(n)]
    return [x, np.dot(phi, w) + Normal(0, a)]