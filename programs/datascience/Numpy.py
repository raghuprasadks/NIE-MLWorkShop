#https://www.datacamp.com/community/tutorials/python-numpy-tutorial
# numpy is Numeric Python” or “Numerical Python”.
# Import `numpy` as `np`
import numpy as np

# Single dimention array
my_array_si = np.array([1,2,3])
print(' single dimention array ', my_array_si)
print(' Data type ', type(my_array_si))
# Print out memory address
print(my_array_si.data)

# Print out the shape of `my_array`
print(my_array_si.shape)

# Print out the data type of `my_array`
print(my_array_si.dtype)

# Print out the stride of `my_array`
#The strides are the number of bytes that should be skipped in memory to go to the next element. 
#If your strides are (10,1), you need to proceed one byte to get to the next column and 10 bytes to locate the next row.
print(my_array_si.strides)
# Make the two dimentional array 
my_array_two = np.array([[1,2,3,4], [5,6,7,8]], dtype=np.int64)
print('two dimentionsional array ', my_array_two)
print(my_array_two.shape)
# Create an array of ones
np.ones((3,4))
# Create an array of zeros
np.zeros((2,3,4),dtype=np.int16)

# Create an array with random values
np.random.random((2,2))
# Create an empty array
np.empty((3,2))
# Create a full array
np.full((2,2),7)
# Create an array of evenly-spaced values
np.arange(10,25,5)
# Create an array of evenly-spaced values
np.linspace(0,2,9)
# Import your data
x, y, z = np.loadtxt('data.txt',
                    skiprows=2,
                    unpack=True)


my_array2 = np.genfromtxt('data2.txt',
                      skip_header=1,
                      filling_values=-999)
# Save text
x = np.arange(0.0,5.0,1.0)
np.savetxt('test.out', x, delimiter=',')
my_array = np.array([1,2,3])
# Print the number of `my_array`'s dimensions
print(my_array.ndim)
# Print the number of `my_array`'s elements
print(my_array.size)
# Print information about `my_array`'s memory layout
print(my_array.flags)
# Print the length of one array element in bytes
print(my_array.itemsize)
# Print the total consumed bytes by `my_array`'s elements
print(my_array.nbytes)
# Print the length of `my_array`
print(len(my_array))
# Change the data type of `my_array`
my_array.astype(float)

# Initialize `x`
x = np.ones((3,4))
# Check shape of `x`
print(x.shape)
# Initialize `y`
y = np.random.random((3,4))
# Check shape of `y`
print(y.shape)
# Add `x` and `y`
x + y

# Initialize `x`
x = np.ones((3,4))

# Check shape of `x`
print(x.shape)
# Initialize `y`
y = np.arange(4)

# Check shape of `y`
print(y.shape)

# Subtract `x` and `y`
x - y 



# Initialize `x` and `y`
x = np.ones((3,4))
y = np.random.random((5,1,4))

# Add `x` and `y`
x + y

my_array = np.array([1,2,3])
my_2d_array = np.array([[1,2,3,4],[5,6,7,8]])
my_3d_array = np.array([[[ 1,2,3,4],[5,6,7,8]],[[1,2,3,4],[9,10,11,12]]])
# Select the element at the 1st index
print(my_array[1])
# Select the element at row 1 column 2
print(my_2d_array[1][2])
# Print `my_2d_array`
print(my_2d_array)
# Transpose `my_2d_array`
print(np.transpose(my_2d_array))
# Or use `T` to transpose `my_2d_array`
print(my_2d_array.T)
# Print the shape of `x`
print(x.shape)
# Resize `x` to ((6,4))
np.resize(x, (6,4))
# Try out this as well
x.resize((6,4))
# Print out `x`
print(x)
# Print the size of `x` to see what's possible
print(x.size)

# Reshape `x` to (2,6)
print(x.reshape((2,6)))

# Flatten `x`
z = x.ravel()

# Print `z`
print(z)



# Append a 1D array to your `my_array`
new_array = np.append(my_array, [7, 8, 9, 10])

# Print `new_array`
print(new_array)

# Append an extra column to your `my_2d_array`
new_2d_array = np.append(my_2d_array, [[7], [8]], axis=1)

# Print `new_2d_array`
print(new_2d_array)

# Insert `5` at index 1
np.insert(my_array, 1, 5)

# Delete the value at index 1
np.delete(my_array,[1])


# Concatentate `my_array` and `x`
print(np.concatenate((my_array,x)))

# Stack arrays row-wise
print(np.vstack((my_array, my_2d_array)))

# Stack arrays row-wise
print(np.r_[my_resized_array, my_2d_array])

# Stack arrays horizontally
print(np.hstack((my_resized_array, my_2d_array)))

# Stack arrays column-wise
print(np.column_stack((my_resized_array, my_2d_array)))

# Stack arrays column-wise
print(np.c_[my_resized_array, my_2d_array])


#How To Visualize NumPy Arrays



# Initialize your array
my_3d_array = np.array([[[1,2,3,4], [5,6,7,8]], [[1,2,3,4], [9,10,11,12]]], dtype=np.int64)

# Pass the array to `np.histogram()`
print(np.histogram(my_3d_array))

# Specify the number of bins
print(np.histogram(my_3d_array, bins=range(0,13)))

import matplotlib.pyplot as plt

# Construct the histogram with a flattened 3d array and a range of bins
plt.hist(my_3d_array.ravel(), bins=range(0,13))

# Add a title to the plot
plt.title('Frequency of My 3D Array Elements')

# Show the plot
plt.show()


# Create an array
points = np.arange(-5, 5, 0.01)

# Make a meshgrid
xs, ys = np.meshgrid(points, points)
z = np.sqrt(xs ** 2 + ys ** 2)

# Display the image on the axes
plt.imshow(z, cmap=plt.cm.gray)

# Draw a color bar
plt.colorbar()

# Show the plot
plt.show()



# Select the element at row 1 column 2
print(my_2d_array[1,2])

# Select the element at row 1, column 2 and 
print(my_3d_array[1,1,2])


# Select items at index 0 and 1
print(my_array[0:2])

# Select items at row 0 and 1, column 1
print(my_2d_array[0:2,1])

# Select items at row 1
# This is the same as saying `my_3d_array[1,:,:]
print(my_3d_array[1,...])

# Try out a simple example
print(my_array[my_array<2])

# Specify a condition
bigger_than_3 = (my_3d_array >= 3)

# Use the condition to index our 3d array
print(my_3d_array[bigger_than_3])

