import numpy as np

arr=np.array([10,20,30,40,50,40,30])
x=np.where(arr==40)
# y=np.searchsorted(arr,30)
y=np.searchsorted(arr,30,side='right')
print(x)
print(y)