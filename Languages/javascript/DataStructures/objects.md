
# JavaScript Object Methods

Here’s a list of commonly used JavaScript object methods, along with examples.

---

## ✅ 1. `Object.keys()`
Returns an array of the object's own enumerable property names.

```js
const obj = { a: 1, b: 2 };
Object.keys(obj);  // ['a', 'b']
```

---

## ✅ 2. `Object.values()`
Returns an array of the object's own enumerable property values.

```js
const obj = { a: 1, b: 2 };
Object.values(obj);  // [1, 2]
```

---

## ✅ 3. `Object.entries()`
Returns an array of key-value pairs.

```js
const obj = { a: 1, b: 2 };
Object.entries(obj);  // [['a', 1], ['b', 2]]
```

---

## ✅ 4. `Object.fromEntries()`
Transforms a list of key-value pairs into an object.

```js
const entries = [['a', 1], ['b', 2]];
Object.fromEntries(entries);  // { a: 1, b: 2 }
```

---

## ✅ 5. `Object.assign()`
Copies enumerable properties from one or more objects to a target object.

```js
const target = { a: 1 };
const source = { b: 2 };
Object.assign(target, source);  // { a: 1, b: 2 }
```

---

## ✅ 6. `Object.freeze()`
Prevents modification of existing properties and values.

```js
const obj = { a: 1 };
Object.freeze(obj);
obj.a = 2;  // No effect
```

---

## ✅ 7. `Object.seal()`
Prevents adding/removing properties but allows modification of existing ones.

```js
const obj = { a: 1 };
Object.seal(obj);
obj.a = 2;     // Works
delete obj.a;  // Fails
```

---

## ✅ 8. `Object.hasOwnProperty()`
Checks whether the object has the specified property as its own property.

```js
const obj = { a: 1 };
obj.hasOwnProperty('a');  // true
```

---

## ✅ 9. `in` Operator
Checks if a property exists in the object (own or inherited).

```js
const obj = { a: 1 };
'a' in obj;  // true
```

---

## ✅ 10. `for...in` Loop
Iterates over enumerable properties.

```js
const obj = { a: 1, b: 2 };
for (let key in obj) {
  console.log(key, obj[key]);
}
```

---

## ✅ 11. `delete` Operator
Removes a property from the object.

```js
const obj = { a: 1, b: 2 };
delete obj.a;  // { b: 2 }
```

---

## ✅ 12. Destructuring Assignment
Extracts properties into variables.

```js
const obj = { a: 1, b: 2 };
const { a, b } = obj;  // a = 1, b = 2
```

---

## ✅ 13. Spread Operator (`...`)
Creates shallow copies or merges objects.

```js
const obj1 = { a: 1 };
const obj2 = { b: 2 };
const merged = { ...obj1, ...obj2 };  // { a: 1, b: 2 }
```

---

## ✅ 14. Optional Chaining (`?.`)
Safely access deeply nested properties.

```js
const user = { profile: { name: 'Abhi' } };
const name = user.profile?.name;  // 'Abhi'
```

---

## ✅ 15. Nullish Coalescing (`??`)
Provides a default value if the left-hand operand is `null` or `undefined`.

```js
const val = null;
const result = val ?? 'default';  // 'default'
```
