
# JavaScript Set Methods

The `Set` object in JavaScript lets you store unique values. Below is a list of commonly used `Set` methods and operations with examples.

---

##  1. `new Set()`
Creates a new Set instance.

```js
const set = new Set([1, 2, 3, 3]);
console.log(set);  // Set(3) {1, 2, 3}
```

---

##  2. `.add(value)`
Adds a new value to the Set.

```js
const set = new Set();
set.add(1);
set.add(2);
console.log(set);  // Set(2) {1, 2}
```

---

##  3. `.has(value)`
Checks if a value exists in the Set.

```js
const set = new Set([1, 2, 3]);
set.has(2);  // true
set.has(5);  // false
```

---

##  4. `.delete(value)`
Removes a value from the Set.

```js
const set = new Set([1, 2, 3]);
set.delete(2);
console.log(set);  // Set(2) {1, 3}
```

---

##  5. `.clear()`
Removes all elements from the Set.

```js
const set = new Set([1, 2]);
set.clear();
console.log(set);  // Set(0) {}
```

---

##  6. `.size`
Returns the number of elements in the Set.

```js
const set = new Set([1, 2, 3]);
console.log(set.size);  // 3
```

---

##  7. Iterating with `for...of`

```js
const set = new Set(["a", "b", "c"]);
for (const item of set) {
  console.log(item);  // 'a', 'b', 'c'
}
```

---

##  8. Convert Set to Array

```js
const set = new Set([1, 2, 3]);
const arr = [...set];  // [1, 2, 3]
```

---

##  9. Convert Array to Set (remove duplicates)

```js
const arr = [1, 2, 2, 3];
const uniqueSet = new Set(arr);  // Set(3) {1, 2, 3}
```

---

##  10. Set Operations (Union, Intersection, Difference)

### Union

```js
const a = new Set([1, 2]);
const b = new Set([2, 3]);
const union = new Set([...a, ...b]);  // Set(3) {1, 2, 3}
```

### Intersection

```js
const intersection = new Set([...a].filter(x => b.has(x)));  // Set(1) {2}
```

### Difference

```js
const difference = new Set([...a].filter(x => !b.has(x)));  // Set(1) {1}
```
