## Inspect attributes of numpy arrays
## Vectors (1D), matrices(2D) and tensors(nD)

import numpy as np

my_1d_list = [1,2,3,4,5]

my_matrix_list=[[1,2,3],[4,5,6],[7,8,9]]

my_tensor_list = [[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]

## Inspect various attributes like size, shape, dimension, datatype, etc

my_vec=np.array(my_1d_list,dtype='int')
my_matrix = np.array(my_matrix_list,dtype='int')
my_tensor = np.array(my_tensor_list,dtype='int')

#Vector attributes

print(my_vec.size, my_vec.shape,my_vec.dtype,my_vec.ndim)

print(my_matrix.size,my_matrix.shape,my_matrix.dtype,my_matrix.ndim)

print(my_tensor.size,my_tensor.shape,my_tensor.dtype,my_tensor.ndim)

