import numpy as np

a=[]
n=int(input("Enter the size : "))
for i in range(n):
	val=int(input("Enter the value: "))
	a.append(val)

arr=np.array(a)
for i in range(arr.size):
	print(arr[i])


arr1=arr[1:2]
print(arr1)