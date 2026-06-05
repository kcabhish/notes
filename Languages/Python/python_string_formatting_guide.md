# Python String Formatting Methods

This guide covers all common ways to format strings in Python, from legacy approaches to modern best practices.

---

## 1. f-Strings (Formatted String Literals) — Recommended

Introduced in Python 3.6, f-strings are the most readable and efficient way to format strings.

```python
name = "Abhishek"
age = 30

result = f"My name is {name} and I am {age} years old."
```

### Expressions inside f-strings
```python
f"Next year, I will be {age + 1}"
```

### Formatting numbers
```python
pi = 3.14159
f"Pi rounded: {pi:.2f}"
```

### Padding and alignment
```python
f"{'hi':>10}"   # right align
f"{'hi':<10}"   # left align
f"{'hi':^10}"   # center
```

### Debugging (Python 3.8+)
```python
f"{name=}, {age=}"
```

---

## 2. str.format() Method

Flexible and widely used before f-strings.

```python
"My name is {} and I am {}".format(name, age)
```

### Positional arguments
```python
"{0} is {1} years old".format(name, age)
```

### Keyword arguments
```python
"{name} is {age} years old".format(name=name, age=age)
```

### Accessing dict values
```python
data = {"name": "Abhishek", "age": 30}
"{name} is {age}".format(**data)
```

### Number formatting
```python
"{:.2f}".format(3.14159)
"{:,}".format(1000000)
```

---

## 3. %-Formatting (Old Style)

Legacy method inspired by C. Avoid in new code.

```python
"My name is %s and I am %d" % (name, age)
```

### Common specifiers
- `%s` → string
- `%d` → integer
- `%f` → float

```python
"%.2f" % 3.14159
```

---

## 4. Template Strings (string.Template)

Useful for user-provided templates or safer substitutions.

```python
from string import Template

t = Template("My name is $name and I am $age")
t.substitute(name="Abhishek", age=30)
```

### Safe substitution
```python
t.safe_substitute(name="Abhishek")
```

---

## 5. format() Built-in Function

Calls an object's __format__ method.

```python
format(3.14159, ".2f")
format(1000000, ",")
```

---

## 6. String Concatenation

Simple but not recommended for formatting complex strings.

```python
"My name is " + name + " and I am " + str(age)
```

---

## 7. join() Method

Efficient way to combine multiple strings.

```python
words = ["Python", "is", "awesome"]
" ".join(words)
```

---

## 8. Advanced Format Specifiers

Used in both f-strings and str.format().

### General syntax
```
{value:flags}
```

### Examples

#### Width and alignment
```python
f"{42:10}"
f"{42:<10}"
f"{42:^10}"
```

#### Zero padding
```python
f"{42:05}"
```

#### Floating point precision
```python
f"{3.14159:.3f}"
```

#### Thousands separator
```python
f"{1000000:,}"
```

#### Percentage
```python
f"{0.25:.2%}"
```

#### Scientific notation
```python
f"{1000:.2e}"
```

---

## 9. Custom Object Formatting (__format__)

You can define how objects are formatted.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __format__(self, format_spec):
        return f"Person({self.name})"

p = Person("Abhishek")
format(p)
```

---

## Summary

| Method            | Recommended | Use Case |
|------------------|------------|----------|
| f-strings        | ✅ Yes     | General use, modern Python |
| str.format()     | ✅ Yes     | Complex formatting, compatibility |
| %-formatting     | ❌ No      | Legacy code only |
| Template strings | ⚠️ Maybe   | User input / templating |
| format()         | ⚠️ Rare    | Low-level formatting |
| join()           | ✅ Yes     | Efficient concatenation |

---

## Best Practice

> Use **f-strings** for almost everything unless you have a specific reason not to.

