import numpy as np


array = np.array([1, 2, 3, 4, 5, 5, 7])
print(*array, sep=', ') 

l = [[1, 2, 3], [4, 5, 6]]
array = np.array([[1, 2, 5], [8, 9, 52], [77, 84, 87]])
print(array)
print('-'*20)
print(l)


#the copy and the view
arr0 = np.array([1, 2, 3])
print(arr0)
print(arr0.view())
arr1 = arr0.view()
arr2 = arr0.copy()
arr1[1]= 50
arr2[1] = 50000
print(arr0)
print(arr1)
print(arr2)



array = np.array([[1, 20000000, 3], [4, 5, 6]])
print(array)


array = np.array([1, 2, 3, 4, 5, 6])
print(array.shape)


#reshape your array from 1D to 2D
array = np.array([1, 2, 3, 4, 5, 6])
print(array.reshape(3, 2))

#reshape your array from 1D to 2D
array = np.array([1, 2, 3, 4, 5, 6])
print(array.reshape((6,1)))


#reshape your array from 1D to another D (with -1)
array = np.array([1, 2, 3, 4, 5, 6])
print(array.reshape((-1,2)))



#The hstack
a = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
aa = np.array([7, 8, 9, 10, 11, 12]).reshape(-1, 1)
print(a)
print('-'*20)
print(aa)
print('-'*20)
print(np.hstack([a, aa]))


#The avantage of numpy, the use of array for addition or multiplication for example
l = [1, 2, 3]
arr = np.array([1, 2, 3])
# print(l + 2)
print(arr + arr)
print(arr + 2)
print(arr * 2)
print(l + l)
print(arr + arr)


#YOUR TURN (10 minutes)
#Change this array [1,5,9,31,45,78]
#into this one:
#[[1 5],
#[9 31],
#[45 78]]
arr = np.array([1,5,9,31,45,78])
print(arr.reshape(-1, 2))