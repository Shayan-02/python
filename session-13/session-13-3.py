import numpy as np
from numpy import random

# print(np.__version__)

# arr1=np.array([1,2,4])
# arr2=np.array([3,5,6])

# print(arr1*2)

# print(arr1*arr2)

# print(arr1[1:4:2])

# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# print(arr)
# print('shape of array :', arr.shape)

# arr = np.array([1, 2, 3, 4, 5, 6])

# newarr = arr.reshape(2, 3)

# print(newarr)

# please create a df from array in which the first 5 numbers are hat sales and the rest is for skirt.

txt="4,5,12,8,9,6,3,9,4,1"

lst=txt.split(',')

#Homework??

print(lst)

arr=np.array([4,5,12,8,9,6,3,9,4,1])

newarr=arr.reshape(2,5)

print(newarr)

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)

print("*****************************************")

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)

arr = np.concatenate((arr1, arr2), axis=0)

print(arr)

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)


#Important , please consider this for next session
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print(x)

# print(833/2)

# print(833%2)

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7, side='left')

print(x)

arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))
print("*****************************************")

x = random.rand()

print(x)


x=random.randint(100, size=(5))

print(x)

x=random.randint(100, size=(5))

print(x)


x = random.randint(100, size=(3, 5))

print(x)

print("$100: ",x[0])
print("$50: ",x[1])
print("$10: ",x[2])


x = random.rand(5)

print(x)

x = random.rand(3, 5)

print(x)

x = random.choice([3, 5, 7, 9])

print(x)

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

print(x)

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))

print(x)

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))

print(x)

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))

print(x)