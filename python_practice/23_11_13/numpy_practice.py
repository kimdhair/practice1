import numpy as np
#1
arr=np.zeros(10)
print(arr)
#2
arr[5]=1
print(arr)
#3
arr1=np.arange(10,31)
print(arr1)
#4
arr2=np.random.randint(0,100,size=(2,2))
print(arr2)
#5
arr3=np.random.rand(2,4)
print(arr3)
#6
arr4=np.arange(35,75)
arr4=arr4.reshape(10,4)
print(arr4)
#7
print("--------------------------")
print(arr4[::-1])
#8
print("--------------------------")
print(arr4[1:-1,2:])
#9
print("--------------------------")