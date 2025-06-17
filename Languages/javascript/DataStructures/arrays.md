
# JavaScript Array Methods

Below is a list of frequently used JavaScript array methods with explanations and examples.

---

## ✅ 1. `map()`
Creates a new array by applying a function to each element.

```js
const nums = [1, 2, 3];
const doubled = nums.map(n => n * 2);  // [2, 4, 6]
```

---

## ✅ 2. `filter()`
Returns a new array with elements that pass the test.

```js
const nums = [1, 2, 3, 4];
const evens = nums.filter(n => n % 2 === 0);  // [2, 4]
```

---

## ✅ 3. `reduce()`
Reduces array to a single value by applying a function.

```js
const nums = [1, 2, 3, 4];
const sum = nums.reduce((acc, cur) => acc + cur, 0);  // 10
```

---

## ✅ 4. `forEach()`
Executes a function for each array element (no return value).

```js
const fruits = ["apple", "banana"];
fruits.forEach(fruit => console.log(fruit));
```

---

## ✅ 5. `find()`
Returns the first element that satisfies a condition.

```js
const nums = [5, 10, 15];
const found = nums.find(n => n > 8);  // 10
```

---

## ✅ 6. `findIndex()`
Returns the index of the first element that satisfies a condition.

```js
const nums = [5, 10, 15];
const index = nums.findIndex(n => n > 8);  // 1
```

---

## ✅ 7. `some()`
Checks if **any** element passes a condition.

```js
const nums = [1, 2, 3];
const hasEven = nums.some(n => n % 2 === 0);  // true
```

---

## ✅ 8. `every()`
Checks if **all** elements pass a condition.

```js
const nums = [2, 4, 6];
const allEven = nums.every(n => n % 2 === 0);  // true
```

---

## ✅ 9. `includes()`
Checks if an array contains a specific value.

```js
const nums = [1, 2, 3];
nums.includes(2);  // true
```

---

## ✅ 10. `sort()`
Sorts elements **in-place**. Caution: mutates original array.

```js
const nums = [3, 1, 2];
nums.sort((a, b) => a - b);  // [1, 2, 3]
```

---

## ✅ 11. `splice()`
Adds/removes items at a specified index. Mutates array.

```js
const arr = [1, 2, 3];
arr.splice(1, 1, 99);  // [1, 99, 3]
```

---

## ✅ 12. `slice()`
Returns a shallow copy of a portion of an array.

```js
const arr = [1, 2, 3, 4];
arr.slice(1, 3);  // [2, 3]
```

---

## ✅ 13. `concat()`
Merges arrays. Returns a new array.

```js
const a = [1, 2];
const b = [3, 4];
const c = a.concat(b);  // [1, 2, 3, 4]
```

---

## ✅ 14. `flat()`
Flattens nested arrays.

```js
const arr = [1, [2, [3]]];
arr.flat(2);  // [1, 2, 3]
```

---

## ✅ 15. `indexOf()` / `lastIndexOf()`
Finds index of a value.

```js
const arr = [1, 2, 3, 2];
arr.indexOf(2);       // 1
arr.lastIndexOf(2);   // 3
```

---

## ✅ 16. `reverse()`
Reverses the array in-place.

```js
const arr = [1, 2, 3];
arr.reverse();  // [3, 2, 1]
```

---

## ✅ 17. `join()`
Converts array to string with a separator.

```js
const arr = ["a", "b", "c"];
arr.join("-");  // "a-b-c"
```

---

## ✅ 18. `push()` / `pop()`
Add/remove elements from the end.

```js
const arr = [1, 2];
arr.push(3);  // [1, 2, 3]
arr.pop();    // [1, 2]
```

---

## ✅ 19. `shift()` / `unshift()`
Add/remove elements from the beginning.

```js
const arr = [1, 2];
arr.unshift(0);  // [0, 1, 2]
arr.shift();     // [1, 2]
```
