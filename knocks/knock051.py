import numpy as np


def exec():
    Z = np.zeros(10, [('position', [('x', float, (1,)),
                                    ('y', float, (1,))]),
                      ('color',    [('r', float, (1,)),
                                    ('g', float, (1,)),
                                    ('b', float, (1,))])])
    print(Z)
