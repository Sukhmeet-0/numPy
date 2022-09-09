import numpy as np

arr=np.arange(1,15)#create array
print(arr)

b=arr>10
print(arr[b])

arr[arr<5]
print(arr[arr<5])


c=arr[arr%2==0]
print(c)