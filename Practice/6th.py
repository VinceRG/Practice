import numpy as np


matrix = np.array ([[1,2],
                    [3,4],
                    [5,6]])
vector = np.array ([7,8])

def transpose():
    a = matrix.shape
    return list(reversed(a))

print(transpose())
