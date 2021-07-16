import numpy as np


def exec():
    D = np.array([0, 1, 2, 3, 15, 16, 32, 64, 128])
    B = ((D.reshape(-1, 1) & (2**np.arange(8))) != 0).astype(int)
    print(B[:, ::-1])
