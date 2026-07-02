# Python Data Structures: List vs Tuple vs Set vs Dictionary

## 🧱 1. List

✅ **Ordered**, ✅ **Mutable**, ❌ **No uniqueness guarantee**

**Definition:** A list is an ordered collection of items that can be
modified (add, remove, or change elements).

**Syntax:**

``` python
fruits = ["apple", "banana", "cherry"]
```

**Key Features:** - Indexed (you can access elements by index) - Allows
duplicates - Mutable (can change after creation)

**Example:**

``` python
fruits.append("orange")
print(fruits[1])  # 'banana'
```

**Use Case:** Use when you need an **ordered**, **modifiable**
collection.

------------------------------------------------------------------------

## 🪄 2. Tuple

✅ **Ordered**, ❌ **Mutable**, ❌ **No uniqueness guarantee**

**Definition:** A tuple is similar to a list but **immutable**.

**Syntax:**

``` python
coordinates = (10, 20)
```

**Key Features:** - Indexed (like lists) - Allows duplicates - Immutable
(cannot add, remove, or change items)

**Example:**

``` python
print(coordinates[0])  # 10
# coordinates[0] = 15 -> TypeError
```

**Use Case:** Use when you want a **constant sequence** of values.

------------------------------------------------------------------------

## ⚙️ 3. Set

❌ **Ordered**, ✅ **Mutable**, ✅ **Unique elements**

**Definition:** A set is an unordered collection of **unique** items.

**Syntax:**

``` python
unique_numbers = {1, 2, 3, 3}
```

**Key Features:** - Unordered (no indexing) - No duplicates - Mutable -
Supports set operations like union, intersection, difference

**Example:**

``` python
unique_numbers.add(4)
unique_numbers.remove(2)
print(2 in unique_numbers)
```

**Use Case:** Use when you need **unique values** or **set operations**.

------------------------------------------------------------------------

## 📘 4. Dictionary

✅ **Key-Value pairs**, ✅ **Mutable**, ✅ **Unique keys**

**Definition:** A dictionary stores data as key-value pairs.

**Syntax:**

``` python
person = {"name": "Alice", "age": 25}
```

**Key Features:** - Unique keys - Mutable - Fast lookup by key

**Example:**

``` python
person["city"] = "New York"
print(person["name"])  # 'Alice'
del person["age"]
```

**Use Case:** Use when you need to **map keys to values**.

------------------------------------------------------------------------

## 🔍 Summary Table

  -----------------------------------------------------------------------------------------------
  Type             Ordered   Mutable   Allows         Indexed   Unique       Example Syntax
                                       Duplicates               Elements     
  ---------------- --------- --------- -------------- --------- ------------ --------------------
  **List**         ✅ Yes    ✅ Yes    ✅ Yes         ✅ Yes    ❌ No        `["a", "b", "c"]`

  **Tuple**        ✅ Yes    ❌ No     ✅ Yes         ✅ Yes    ❌ No        `("a", "b", "c")`

  **Set**          ❌ No     ✅ Yes    ❌ No          ❌ No     ✅ Yes       `{1, 2, 3}`

  **Dictionary**   ✅ Yes\*  ✅ Yes    Keys ❌ /      ✅ Keys   ✅ Keys      `{"a": 1, "b": 2}`
                                       Values ✅                             
  -----------------------------------------------------------------------------------------------

> \*Since Python 3.7+, dictionaries maintain insertion order, but
> they're still key-based.

------------------------------------------------------------------------

## ⚡ Performance Comparison (Time Complexity)

  -----------------------------------------------------------------------------
  Operation           **List**     **Tuple**     **Set**      **Dictionary**
  ------------------ ----------- -------------- ---------- --------------------
  **Access by           O(1)          O(1)         N/A             O(1)
  index/key**                                              

  **Search (by          O(n)          O(n)      O(1) avg /   O(1) avg / O(n)
  value)**                                      O(n) worst        worst

  **Insert /           O(1)\*     ❌ Immutable   O(1) avg        O(1) avg
  Append**                                                 

  **Delete /            O(n)      ❌ Immutable  O(1) avg /       O(1) avg
  Remove**                                      O(n) worst 

  **Iteration           O(n)          O(n)         O(n)            O(n)
  (looping)**                                              

  **Memory usage**      High          Low         Medium           High

  **Immutability**     Mutable     Immutable     Mutable         Mutable
  -----------------------------------------------------------------------------

> \*List `append()` is amortized O(1); rare resizing takes longer.

------------------------------------------------------------------------

## 🧠 Quick Summary

  ------------------------------------------------------------------------
  Data Type        Best For      Fastest Operations       Avoid When
  ---------------- ------------- ------------------------ ----------------
  **List**         Ordered,      Append, iterate          When you need
                   sequential                             fast lookups
                   data                                   

  **Tuple**        Fixed,        Access                   You need to
                   constant data                          modify data

  **Set**          Unique items, `in`, add/remove         You need
                   fast                                   ordering
                   membership                             

  **Dictionary**   Key-value     Lookup by key            You don't have
                   mapping                                meaningful keys
  ------------------------------------------------------------------------
