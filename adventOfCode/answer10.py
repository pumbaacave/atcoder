"""
copy from https://www.reddit.com/r/adventofcode/comments/a4urh5/day_10_in_only_8_iterations_with_gradient_descent/
"""
x = []
v = []

with open('input10', 'r') as f:
    for line in f:
        x.append((int(line[10:16]), int(line[18:24])))
        v.append((int(line[36:38]), int(line[40:42])))

import numpy as np
x = np.array(x)
v = np.array(v)

import matplotlib.pyplot as plt

def extent(t):
    locs = x + t*v
    return sum(np.max(locs, axis=0) - np.min(locs, axis=0))

from scipy.optimize import minimize
# %timeit minimize(extent, 0)
t = minimize(extent, 0)
nit = t.nit
t = int(np.round(t.x))

print(t, nit)

plt.plot(*(x + t*v).T, ls='', marker='o', color='k')
plt.gca().invert_yaxis()
plt.axis('equal')
plt.show()
