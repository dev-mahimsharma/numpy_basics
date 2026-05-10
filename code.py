import numpy as np

# python list 
py_list =[1,2,3,4,5,6]

# print(py_list *2)

# numpy array 

arr =np.array([1,2,3])

# print(arr *2)


# print(type(arr))
# print(type(py_list))

zero_dimension_array =np.array("A")


# prints the dimension of the array (.ndim)
# print(zero_dimension_array.ndim)

two_dimension_array =np.array([[1,2,3],[4,5,6]])

# prints the dimension of the array (.ndim)
# print(two_dimension_array.ndim)

three_dimension_array =np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]], [[1,2,3],[4,5,6],[7,8,9]]])

# prints the dimension of the array (.ndim)
# print(three_dimension_array.ndim)

# prints the shape tuple of an array
# print(three_dimension_array.shape)



