import numpy as np


def exec():
    Z = np.random.randint(0, 2, (6, 3))
    T = np.ascontiguousarray(Z).view(
        np.dtype((np.void, Z.dtype.itemsize * Z.shape[1])))
    _, idx = np.unique(T, return_index=True)
    uZ = Z[idx]
    print(uZ)
