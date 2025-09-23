## PRANAV GUNDRALA ## APMA1690 ## FALL 2025 ##
import numpy as np
from numpy import random
from matplotlib import pylab as plt
from matplotlib import patches

# function to estimate pi for N points
def compute_pi(N:int, seed:int=42):
    random.seed(seed)
    # sample uniform tuples (x, y) from [-1:1]
    points = random.uniform(-1, 1, N*2)
    points = np.reshape(points, (N, 2))

    # find inside unit circle C: x^2 + y^2 <= 1
    C = points[points[:,0]**2 + points[:,1]**2 <= 1, :]
    S = points[points[:,0]**2 + points[:,1]**2 > 1, :]
    # compare inside/outside to get pi/4
    pi = (C.shape[0]/N)*4

    return C, S, pi

# calculate for N = 50, 100, ..., 5000
# exclude 0 b/c of divide by zero error
N = range(50, 5050, 50)
estimates = [compute_pi(n)[2] for n in N]

# NOTE: the estimates seem to quickly approach pi, and
# level off as N gets larger (see trend in plot)

# # plot
plt.style.use('ggplot')
plt.scatter(N, estimates, marker='x', color='blue', alpha=0.7)
plt.xlabel('uniform sampled points (N) in unit square')
plt.ylabel('ratio of points inside unit circle')
plt.savefig('pi_estimates.png', dpi=300, bbox_inches="tight")
plt.clf()

# square/circle plot
C = compute_pi(100)[0]
S = compute_pi(100)[1]
x_inside, y_inside = C[:, 0], C[:, 1]
x_outside, y_outside = S[:, 0], S[:, 1]

fig, ax = plt.subplots()
circle = plt.Circle((0,0), 1, alpha=0.5, fc='none', ec='blue', lw=1)
square = plt.Rectangle((-1,-1), 2, 2, alpha=0.5, fc='none', ec='red', lw=1)
ax.add_patch(square)
ax.add_patch(circle)
fig.set_figheight(5)
fig.set_figwidth(5)
plt.plot(x_inside, y_inside, 'o', color='blue', ms=4)
plt.plot(x_outside, y_outside, 'o', color='red', ms=4)
plt.savefig('pi_graph.png', dpi=300, bbox_inches="tight")