import numpy as np

arr=np.arange(1,5)
print(arr*2)
print(arr**2)
print(arr/0)


a=np.array([1,2,3,4]).reshape(2,2)
b=np.array([5,6,7,8]).reshape(2,2)

print(a+b)
print(a.dot(b))