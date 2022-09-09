import numpy as np

np.random.seed(122)
matrix=np.random.randint(1,21,9).reshape(3,3)

print(np.sum(matrix))
print(matrix.sum())
print(np.min(matrix))
print(np.max(matrix))
print(np.max(matrix,axis=1))
print(np.sum(matrix,axis=0))
print(np.cumsum(matrix))