
# Vectors and Matrices

## 1. Vector

A **vector** is an **ordered list of numbers** — basically a **1D array**.  
It represents a quantity that has **both magnitude and direction** (in math or physics) or just a **collection of related values** (in programming or data science).  

### Examples

In math:
```
v = [2, 5, 3]
```
This is a **3-dimensional vector** (three numbers stacked vertically).

In programming (like Python/NumPy):
```python
import numpy as np
v = np.array([2, 5, 3])
```

You can think of a vector as:
- A **point in space** (x, y, z)
- A **row or column** in a spreadsheet
- A **feature set** in machine learning (e.g., [height, weight, age])

---

## 2. Matrix

A **matrix** is a **2D array of numbers** — basically a collection of **rows and columns of vectors**.  
It’s used to represent **linear transformations**, **datasets**, or **systems of equations**.

### Example

```
A = [
  [1, 2, 3],
  [4, 5, 6]
]
```
- Matrix `A` has **2 rows** and **3 columns** → size **2×3** (read as “2 by 3”).
- Each **row** can be seen as a **vector**.

In Python:
```python
A = np.array([[1, 2, 3],
              [4, 5, 6]])
```

---

## 3. Relationship Between Them

A **vector** is a **special case of a matrix**:
- A **row vector** → a matrix with 1 row.
- A **column vector** → a matrix with 1 column.

Example:
```
Column Vector:
[
  [2],
  [5]
]
```
is the same as a **2×1 matrix**.

---

## 4. Quick Summary

| Concept | Dimensions | Example | In Python (NumPy) |
|----------|-------------|----------|------------------|
| **Vector** | 1D | [2, 5, 3] | `np.array([2, 5, 3])` |
| **Matrix** | 2D | [[1,2,3],[4,5,6]] | `np.array([[1,2,3],[4,5,6]])` |
