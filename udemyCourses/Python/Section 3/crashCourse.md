# Python Revision

## Variable Declaration


```Python
x= 12
name = 'John Doe'
print ('My number is {} and my name is {}', format(x,name))
```

Alternatively we can also use the format string to assign values.

```Python
x= 12
name = 'John Doe'
print ('My number is {one} and my name is {two}', format(two='Peter Parker', one=7))
```

Using the variable assignmnet gives the flexibility to use multiple variables when using the string fromat method. For example:
```Python
print ('My number is {one} and my name is {two}. {two} is also the spider man.', format(two='Peter Parker', one=7))
```

## String

```Python
sampleString = 'abcdefghij'
# grabs all elements from index 3
print (sampleString[3:]) # defgghi
# grabs all elements before index 3
print(sampleString[:3]) # abc
# grabs elements from index 3 upto 5
print(sampleString[3:6])  # def
```

## List || Array

Mutable: Lists can be modified after creation. Elements can be added, removed, or changed.

```python
my_list = ['a', 'b', 'c']
my_list.append('d') # adding element to list
```

## Tuple

Immutable: Tuples cannot be modified after creation. Their elements cannot be added, removed, or changed.

```python
my_tuple = ('a', 'b','c')
print(my_tuple[0])
```

## When to choose a tuple or a list
### Choose a tuple when:
- You have a collection of items that should not change throughout the life of the program, such as coordinates (x, y, z) or RGB color values (255, 165, 0).
- You need to use the collection as a key in a dictionary or as an element in a set.
A function needs to return multiple values. Python will automatically pack these values into a tuple.
- You are defining a constant set of values that will only be iterated over, which can provide a slight performance and memory advantage. 
### Choose a list when:
- You need to add, remove, or change elements in the collection.
- The size of the collection is dynamic and will change during the program's execution.
- You need to sort or otherwise manipulate the order of the elements.
- You are storing a homogeneous collection of items, and the order is important but not rigidly fixed by type.