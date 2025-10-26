# NumPy

[Link](https://numpy.org/doc/stable/index.html) to the official docs.

## Installing numpy

```
conda install numpy
```
Or
```
pip install numpy
```

## Check numpy
To check numpy version.

```
conda list numpy
```

Or
```
pip show numpy
```

## Using Numpy

`import numpy as np`

## Numpy arrays

- Numpy arrays essentially come in two flavors: vectors an matrices.
- Vectors are strictly 1-d arrays and matcirces are 2-d (matrices can still have only one row or one column)

example
```Python
my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
my_matrix

# OUTPPUT
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

np.array(my_matrix)
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
```

## [Shape Size And Dimensions](https://numpy.org/doc/stable/user/absolute_beginners.html#how-do-you-know-the-shape-and-size-of-an-array)
`array.ndim` returns the dimension of the array
`array.size` returns the total number of elements
`array.shape` returns the shape of the array
example
```Python
array_example = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0 ,1 ,2, 3],
                           [4, 5, 6, 7]]])

array_example.ndim  # returns 3
array_example.size  # returns 24
array_example.shape # returns (3,2,4)

```

## Indexing and Slicing

```Python
data = np.array([1, 2, 3, 4])

data[1]
# 2
data[0:2]
# [1,2]
data[1:]
# [2,3,4]
data[-2:]
#[3,4]
data[:]
# [1,2,3,4]
```

## Broadcasting

There are times when you might want to carry out an operation between an array and a single number (also called an operation between a vector and a scalar) or between arrays of two different sizes. For example, your array (we’ll call it “data”) might contain information about distance in miles but you want to convert the information to kilometers. You can perform this operation with:

```Python
data = np.array([1.0, 2.0])
data * 1.6
# this will boradcast all the array to be in kilometeres
array([1.6, 3.2])
```
