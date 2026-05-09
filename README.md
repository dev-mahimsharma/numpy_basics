# NumPy Quick Guide

NumPy is the core Python library for fast numerical computing. It gives you the
`ndarray`, a powerful multi-dimensional array object, plus many functions for
math, statistics, indexing, reshaping, random numbers, and linear algebra.

## Installation

```bash
pip install numpy
```

Basic import:

```python
import numpy as np
```

## Why Use NumPy?

- It is much faster than normal Python lists for numerical work.
- It supports multi-dimensional arrays like vectors, matrices, and tensors.
- It provides vectorized operations, so you can avoid many slow Python loops.
- It is the foundation for libraries like pandas, scikit-learn, SciPy,
  TensorFlow, PyTorch, and many data science tools.

## Important Concepts

### NumPy Array

The main object in NumPy is the `ndarray`.

```python
arr = np.array([1, 2, 3, 4])
print(arr)
```

### Shape

The shape tells you the size of each dimension.

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)  # (2, 3)
```

### Dimensions

The number of dimensions is called `ndim`.

```python
print(arr.ndim)  # 2
```

### Data Type

Every NumPy array has one data type.

```python
print(arr.dtype)
```

Common dtypes:

- `int64`
- `float64`
- `bool`
- `str`
- `complex`

### Vectorization

Vectorization means applying operations to whole arrays at once.

```python
arr = np.array([1, 2, 3])
print(arr * 10)  # [10 20 30]
```

This is usually faster and cleaner than using loops.

### Broadcasting

Broadcasting lets NumPy work with arrays of different shapes when their shapes
are compatible.

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr + 10)
```

Example with two arrays:

```python
matrix = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([10, 20, 30])

print(matrix + vector)
```

## Creating Arrays

```python
np.array([1, 2, 3])              # Create array from list
np.zeros((2, 3))                 # 2x3 array of zeros
np.ones((2, 3))                  # 2x3 array of ones
np.full((2, 3), 7)               # 2x3 array filled with 7
np.empty((2, 3))                 # Uninitialized array
np.arange(0, 10, 2)              # [0 2 4 6 8]
np.linspace(0, 1, 5)             # 5 evenly spaced values from 0 to 1
np.eye(3)                        # 3x3 identity matrix
np.random.rand(2, 3)             # Random floats from 0 to 1
np.random.randint(1, 10, (2, 3)) # Random integers
```

## Indexing and Slicing

```python
arr = np.array([10, 20, 30, 40, 50])

arr[0]      # First item
arr[-1]     # Last item
arr[1:4]    # Items from index 1 to 3
arr[:3]     # First three items
arr[::2]    # Every second item
```

For 2D arrays:

```python
matrix = np.array([[1, 2, 3], [4, 5, 6]])

matrix[0, 1]    # Row 0, column 1
matrix[:, 0]    # First column
matrix[1, :]    # Second row
```

## Boolean Indexing

```python
arr = np.array([1, 2, 3, 4, 5, 6])

print(arr[arr > 3])        # [4 5 6]
print(arr[arr % 2 == 0])   # [2 4 6]
```

## Reshaping Arrays

```python
arr = np.arange(12)

arr.reshape(3, 4)   # Convert to 3x4
arr.reshape(2, 6)   # Convert to 2x6
arr.flatten()       # Convert to 1D copy
arr.ravel()         # Convert to 1D view when possible
```

Use `-1` to let NumPy calculate the missing size:

```python
arr.reshape(3, -1)
```

## Combining Arrays

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

np.concatenate([a, b])     # [1 2 3 4 5 6]
np.stack([a, b])           # Stack into new dimension
np.vstack([a, b])          # Stack vertically
np.hstack([a, b])          # Stack horizontally
```

## Splitting Arrays

```python
arr = np.array([1, 2, 3, 4, 5, 6])

np.split(arr, 3)       # Split into 3 equal parts
np.array_split(arr, 4) # Split into 4 parts, even if not equal
```

## Math Operations

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

a + b      # Add
a - b      # Subtract
a * b      # Multiply element-wise
a / b      # Divide element-wise
a ** 2     # Power
```

Useful math functions:

```python
np.sqrt(a)      # Square root
np.exp(a)       # e^x
np.log(a)       # Natural log
np.sin(a)       # Sine
np.cos(a)       # Cosine
np.abs(a)       # Absolute value
np.round(a)     # Round values
np.floor(a)     # Round down
np.ceil(a)      # Round up
```

## Aggregation Functions

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

np.sum(arr)       # Sum of all values
np.mean(arr)      # Average
np.median(arr)    # Median
np.min(arr)       # Minimum
np.max(arr)       # Maximum
np.std(arr)       # Standard deviation
np.var(arr)       # Variance
np.prod(arr)      # Product
```

Use `axis` to calculate across rows or columns:

```python
np.sum(arr, axis=0)  # Column-wise sum
np.sum(arr, axis=1)  # Row-wise sum
```

## Sorting and Searching

```python
arr = np.array([3, 1, 5, 2, 4])

np.sort(arr)          # Sorted values
np.argsort(arr)       # Indexes that would sort the array
np.argmax(arr)        # Index of max value
np.argmin(arr)        # Index of min value
np.where(arr > 3)     # Indexes where condition is true
np.unique(arr)        # Unique values
```

## Copy vs View

This is important.

```python
arr = np.array([1, 2, 3])

view = arr[0:2]       # Usually a view
copy = arr.copy()     # Independent copy
```

A view shares memory with the original array. A copy does not.

```python
view[0] = 99
print(arr)  # Original array may change
```

Use `.copy()` when you need an independent array.

## Linear Algebra

```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

np.dot(a, b)          # Dot product / matrix multiplication
a @ b                # Matrix multiplication
np.linalg.inv(a)      # Inverse matrix
np.linalg.det(a)      # Determinant
np.linalg.eig(a)      # Eigenvalues and eigenvectors
np.linalg.solve(a, b) # Solve linear equations
```

## Random Numbers

Modern NumPy recommends using `default_rng`.

```python
rng = np.random.default_rng(seed=42)

rng.random(5)              # 5 random floats from 0 to 1
rng.integers(1, 10, 5)     # 5 random integers from 1 to 9
rng.normal(0, 1, 5)        # Normal distribution
rng.choice([1, 2, 3], 5)   # Random choices
rng.shuffle(arr)           # Shuffle array in place
```

## Handling Missing or Special Values

```python
arr = np.array([1, 2, np.nan, 4])

np.isnan(arr)       # Check for NaN
np.nanmean(arr)     # Mean ignoring NaN
np.nansum(arr)      # Sum ignoring NaN
np.isinf(arr)       # Check for infinity
np.isfinite(arr)    # Check for normal finite values
```

## Useful NumPy Functions Cheat Sheet

| Function | Description |
| --- | --- |
| `np.array()` | Creates a NumPy array from a list or tuple. |
| `np.zeros()` | Creates an array filled with zeros. |
| `np.ones()` | Creates an array filled with ones. |
| `np.full()` | Creates an array filled with a specific value. |
| `np.empty()` | Creates an uninitialized array. |
| `np.arange()` | Creates values with a fixed step size. |
| `np.linspace()` | Creates evenly spaced values over a range. |
| `np.eye()` | Creates an identity matrix. |
| `np.reshape()` | Changes the shape of an array. |
| `np.ravel()` | Flattens an array, returning a view when possible. |
| `np.flatten()` | Flattens an array, returning a copy. |
| `np.concatenate()` | Joins arrays along an existing axis. |
| `np.stack()` | Joins arrays along a new axis. |
| `np.vstack()` | Stacks arrays vertically. |
| `np.hstack()` | Stacks arrays horizontally. |
| `np.split()` | Splits an array into equal parts. |
| `np.array_split()` | Splits an array into parts that may be unequal. |
| `np.sum()` | Adds values. |
| `np.mean()` | Calculates average. |
| `np.median()` | Calculates median. |
| `np.min()` | Finds minimum value. |
| `np.max()` | Finds maximum value. |
| `np.std()` | Calculates standard deviation. |
| `np.var()` | Calculates variance. |
| `np.prod()` | Multiplies all values. |
| `np.sqrt()` | Calculates square root. |
| `np.exp()` | Calculates exponential value. |
| `np.log()` | Calculates natural logarithm. |
| `np.abs()` | Calculates absolute value. |
| `np.round()` | Rounds values. |
| `np.floor()` | Rounds values down. |
| `np.ceil()` | Rounds values up. |
| `np.sort()` | Sorts array values. |
| `np.argsort()` | Returns indexes that sort the array. |
| `np.argmax()` | Returns index of maximum value. |
| `np.argmin()` | Returns index of minimum value. |
| `np.where()` | Returns values or indexes based on a condition. |
| `np.unique()` | Returns unique values. |
| `np.copy()` | Creates an independent copy. |
| `np.dot()` | Calculates dot product. |
| `np.matmul()` | Performs matrix multiplication. |
| `np.transpose()` | Swaps array axes. |
| `np.isnan()` | Checks for NaN values. |
| `np.nanmean()` | Calculates mean while ignoring NaN. |
| `np.isfinite()` | Checks for finite values. |
| `np.save()` | Saves array to `.npy` file. |
| `np.load()` | Loads array from `.npy` file. |
| `np.savetxt()` | Saves array to text or CSV file. |
| `np.loadtxt()` | Loads data from text file. |

## Saving and Loading Arrays

Save as NumPy binary:

```python
arr = np.array([1, 2, 3])

np.save("data.npy", arr)
loaded = np.load("data.npy")
```

Save as text:

```python
np.savetxt("data.csv", arr, delimiter=",")
loaded = np.loadtxt("data.csv", delimiter=",")
```

## Common Mistakes

### Forgetting That Operations Are Element-Wise

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a * b)  # Element-wise multiplication
```

For matrix multiplication, use:

```python
a @ b
np.dot(a, b)
```

### Shape Mismatch

Arrays must have compatible shapes for operations.

```python
a = np.array([1, 2, 3])
b = np.array([1, 2])

# a + b will fail because shapes are not compatible
```

Check shapes with:

```python
print(a.shape)
print(b.shape)
```

### Modifying Views Accidentally

Slicing often returns a view, not a copy.

```python
arr = np.array([1, 2, 3, 4])
part = arr[:2]
part[0] = 99

print(arr)  # arr changed
```

Use this when you want a separate array:

```python
part = arr[:2].copy()
```

## Mini Examples

### Normalize Values

```python
arr = np.array([10, 20, 30, 40])
normalized = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))

print(normalized)
```

### Filter Values

```python
arr = np.array([5, 10, 15, 20, 25])
filtered = arr[arr >= 15]

print(filtered)
```

### Calculate Column Averages

```python
data = np.array([
    [80, 90, 70],
    [75, 85, 95],
    [60, 70, 80],
])

print(np.mean(data, axis=0))
```

### Replace Values Using `where`

```python
arr = np.array([1, 2, 3, 4, 5])
result = np.where(arr % 2 == 0, "even", "odd")

print(result)
```

## Best Practices

- Use `import numpy as np`.
- Prefer vectorized operations over loops.
- Always check `.shape` when debugging array errors.
- Use `axis=0` for column-wise operations and `axis=1` for row-wise operations.
- Use `.copy()` when you do not want changes to affect the original array.
- Use `np.random.default_rng()` for new random number code.
- Use NumPy for numeric arrays, not for mixed data like names and addresses.

## Quick Practice Ideas

1. Create a 3x3 matrix of numbers from 1 to 9.
2. Find the mean of each row.
3. Find all values greater than 5.
4. Reshape a 1D array of 12 numbers into a 3x4 matrix.
5. Generate 10 random numbers and sort them.
6. Replace all negative values in an array with 0.
7. Save an array to a file and load it again.

