import numpy as np

arr=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])

print(arr)
print(arr2)

print(np.hstack((arr,arr2)))
print(np.vstack((arr,arr2)))


np.random.seed(122)
a=np.random.randint(1,21,9).reshape(3,3)
b=np.random.randint(50,71,9).reshape(3,3)

print(np.hstack((a,b)))