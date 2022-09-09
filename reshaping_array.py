import numpy as np

arr=np.random.randint(1,50,12)
print(arr)

arr=arr.reshape(2,6)
print(arr)

arr=arr.reshape(4,3)
print(arr)
print("Shape = ",arr.shape)