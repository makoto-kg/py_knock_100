import numpy as np


def exec():
    Z = np.random.randint(0, 5, (10, 3))
    print(Z)
    E = np.all(Z[:, 1:] == Z[:, :-1], axis=1)
    U = Z[~E]
    print(U)
