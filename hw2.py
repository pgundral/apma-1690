## PRANAV GUNDRALA ## APMA1690 ## FALL 2025 ##
import numpy as np
from numpy import random
from matplotlib import pylab as plt

def compute_pi(N:int, seed:int=42):
    random.seed(seed)
    points = random.uniform(-1, 1, N*2)
    points = np.reshape(points, (N, 2))

    # inside unit circle C
    C = points[np.sqrt(points[:,0]**2 + points[:,1]**2) <= 1, :]
    pi = (C.shape[0]/N)*4

    return pi

N = range(50, 5050, 50)
estimates = [compute_pi(n) for n in N]

plt.scatter(N, estimates)

plt.show()