import numpy as np

arr=np.zeros(5)
a=np.zeros((2,3))
print(arr)
print(a)

b=np.ones(5)
print(b)

c=np.eye(3,4)
print(c)
# c=np.eye((4))
# print(c)

d=np.diag([2,3,4])
print(d)

e=np.random.randint(0,14,3)
print(e)

f=np.random.rand(2,3)
print(f)

g=np.random.randn(5)
print(g)