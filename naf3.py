import numpy as np

np.random.seed(122)
arr=np.random.randint(1,21,10)
print(arr)

np.random.shuffle(arr)
print(arr)

print(np.unique(arr))

print(np.unique(arr).size)

print(np.unique(arr,return_index=True,return_counts=True))

