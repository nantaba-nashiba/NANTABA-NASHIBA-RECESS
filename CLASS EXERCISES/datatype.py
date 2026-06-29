import numpy as np

# Data type of a NumPy array
z = np.array([5, 6, 9])
print('z:', z)
print('dtype of z:', z.dtype)

# Create a NumPy array from a Python list
array1 = np.array([8, 2, 5])
print('array1:', array1)
print('dtype of array1:', array1.dtype)

# Create an array filled with zeros
zero_array = np.zeros((4, 5))
print('zero_array:')
print(zero_array)
print('dtype of zero_array:', zero_array.dtype)

# Create a random array with shape (3, 6)
random_array = np.random.rand(3, 6)
print('random_array:')
print(random_array)
print('dtype of random_array:', random_array.dtype)

print(np.eye(3))  # Create a 3x3 identity matrix