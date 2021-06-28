import numpy as np
from knocks.knock078 import distance


def exec():
    P0 = np.random.uniform(-10, 10, (10, 2))
    P1 = np.random.uniform(-10, 10, (10, 2))
    p = np.random.uniform(-10, 10, (10, 2))
    print(np.array([distance(P0, P1, p_i) for p_i in p]))
