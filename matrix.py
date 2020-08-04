import numpy as np
np.random.seed(1010)
A = np.random.normal(-1, 1, size=12).reshape(3, 4)
B = np.random.normal(1, 1, size=12).reshape(4, 3)
C = 2*A + 3*B.T
print(A)
print(B)
print(C)
