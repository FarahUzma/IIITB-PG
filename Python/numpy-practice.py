import numpy as np

print(np.__version__)

my_list = [1,2,3,4]
array = np.array(my_list)
array = array * 2
print(array)
print(type(array))

array = np.array(['A','B','C'])

print(array.ndim)
print(array.shape)

array2 = np.array([['A','B','C'],['A','B','C']])
print(array2.ndim)
print(array2.shape)


array3 = np.array([[['A','B','C'],['A','B','C']],[['A','B','C'],['A','B','C']]])
print(array3.ndim)
print(array3.shape)

