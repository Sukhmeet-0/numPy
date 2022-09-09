import numpy as np

a=np.array([[10,20,30],[40,50,60],[70,80,90]])
print(a)

print(a[:2,:1])

np.random.seed(111)
a=np.random.randint(1,500,30).reshape(6,5)
print(a)

print(a[:3,:3])