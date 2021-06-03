import numpy as np
from io import StringIO


def exec():
    s = StringIO('''1, 2, 3, 4, 5
                    6, , , 7, 8
                    , , 9,10,11
    ''')
    Z = np.genfromtxt(s, delimiter=",", dtype=np.int)
    print(Z)
