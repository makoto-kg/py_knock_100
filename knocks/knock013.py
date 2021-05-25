import numpy as np


def exec():
    z = np.random.random((10, 10))
    z_min, z_max = z.min(), z.max()
    print(z_min, z_max)
