import numpy as np


def exec():
    A = np.random.uniform(0, 1, 10)
    B = np.random.uniform(0, 1, 10)
    print(np.einsum('i->', A))
    print(np.einsum('i,i->i', A, B))
    print(np.einsum('i,i', A, B))
    print(np.einsum('i,j->ij', A, B))
