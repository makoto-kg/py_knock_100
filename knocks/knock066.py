import numpy as np


def exec():
    w, h = 256, 256
    data = np.random.randint(0, 4, (h, w, 3)).astype(np.ubyte)
    colors = np.unique(data.reshape(-1, 3), axis=0)
    n = len(colors)
    print(n)
