import numpy as np

my_np_arr= np.array([[3,5,6,8,9,1,2],[2,4,3,5,6,7,8]])

print(my_np_arr.shape)

#2D arrays
#create 2d array from diff lists
list1 = [1,2,3] #row1
list2 = [4,5,6] #row2
list3 = [7,8,9] #row3

arr = np.array([list1,list2,list3])

print(arr)
#treat above lists as columns

arr = np.array([list1,list2,list3]).T

print(arr)

#creating array from a shape and value

shape = (3,5)
value = 5
arr = np.full(shape,value)
print(arr)

arr = np.zeros(shape)
print(arr)

arr = np.ones(shape)
print(arr)

#creating array from random numbers

arr_rand = np.random.rand(3,5)
print(arr_rand)

#creating diagonal matrix from 1D array

arr_diag = np.diag([1,2,3,4])
print(arr_diag)

#creating an array for a sequence of nmbers/range

arr_range = np.arange(0,1001,1)
print(arr_range)

arr_range = np.arange(1001)
print(arr_range)

### Arrays with data types, int or float

my_list = [1,2,3,4,5]

int_arr = np.array(my_list,dtype='int')
print(int_arr)

f_arr = np.array(my_list,dtype='float')
print(f_arr)

f_arr = np.zeros((2,3),dtype='float')
print(f_arr)

f_arr = np.ones((2,3),dtype='float')
print(f_arr)

f_arr_full = np.full((3,5),5.4,dtype='float')
print(f_arr_full)

##### Updating values inside numpy array

f_arr_full[1,1]=6
print(f_arr_full)