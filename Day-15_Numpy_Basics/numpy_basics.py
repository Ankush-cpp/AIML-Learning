# NumPy Basics & Slicing
import numpy as np

# 1. Creating Arrays

arr1 = np.array([10, 20, 30, 40, 50])
print("1D Array:")
print(arr1)

# 2D Array

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("\n2D Array:")
print(arr2)

# 2. Array Information

print("\nShape of arr2:", arr2.shape)
print("Dimensions:", arr2.ndim)
print("Data Type:", arr2.dtype)
print("Size:", arr2.size)

# 3. Indexing

print("\nFirst Element:", arr1[0])
print("Last Element:", arr1[-1])

# 2D Indexing

print("\nElement at row 1 col 2:", arr2[1][2])

# 4. Slicing

print("\nArray Slicing:")
print("Elements from index 1 to 3:")
print(arr1[1:4])

print("\nFirst 3 elements:")
print(arr1[:3])

print("\nElements after index 2:")
print(arr1[2:])

print("\nReverse Array:")
print(arr1[::-1])

print("\nEvery 2nd element:")
print(arr1[::2])

# 5. 2D Array Slicing

print("\nFirst Row:")
print(arr2[0])

print("\nSecond Column:")
print(arr2[:, 1])

print("\nFirst 2 Columns:")
print(arr2[:, :2])

# 6. Array Operations

print("\nAddition:")
print(arr1 + 10)

print("\nMultiplication:")
print(arr1 * 2)

print("\nSquare:")
print(arr1 ** 2)

# 7. Special Arrays

print("\nZeros Array:")
print(np.zeros((2, 2)))

print("\nOnes Array:")
print(np.ones((3, 3)))

# 8. Range Functions

print("\nUsing arange:")
print(np.arange(0, 10, 2))

print("\nUsing linspace:")
print(np.linspace(0, 1, 5))

# 9. Reshape

arr3 = np.arange(1, 13)
reshaped = arr3.reshape(3, 4)

print("\nReshaped Array:")
print(reshaped)

# 10. Max / Min / Sum / Mean

print("\nMaximum:", arr1.max())
print("Minimum:", arr1.min())
print("Sum:", arr1.sum())
print("Mean:", arr1.mean())

# 11. Boolean Filtering

print("\nElements greater than 25:")
print(arr1[arr1 > 25])

# 12. Copy vs View

view_arr = arr1.view()
copy_arr = arr1.copy()

print("\nOriginal Array:")
print(arr1)

print("\nView Array:")
print(view_arr)

print("\nCopy Array:")
print(copy_arr)