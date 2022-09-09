import numpy as np

a=np.array([10,20,30,40,50,60,70,80])
# slicing=a[3:60]
slicing=a[3:60].copy()
print(slicing)
slicing[:]=0
print(a)