# Introduction

[Kotlin](https://kotlinlang.org/)

[Getting Started With Kotlin](https://kotlinlang.org/docs/getting-started.html)

[Download JDK](https://www.oracle.com/java/technologies/downloads/#java8)

[IDE Intelij IDEA](https://www.jetbrains.com/idea/)

## Kotlin REPL

In the Intelij IDE you can run REPL to try some of the Kotlin commands. To navigate to REPL:

1. Open Tools from the menu bar.
2. Naivigate to Kotlin dropdown.
3. Select REPL

it will open a terminal and users can start experimenting with the Kotlin command and pressing `ctrl+Enter` to evaluate the expressions.

## Variables

In Kotlin variables can be declared using the var key word or val keyword. The variables created using var can be modifed but the variables created using var are constants.

```
var name = "John Doe"
val pi = 3.1416
```
In the above example, name can be updated by reassigning a value but pi cannot.

## Primitive Types & Strings

[Kotling Data Types](https://kotlinlang.org/docs/basic-types.html)

This section describes the basic types used in Kotlin:

- [Numbers](https://kotlinlang.org/docs/numbers.html#integer-types) and their unsigned counterparts
- [Booleans](https://kotlinlang.org/docs/booleans.html)
- [Characters](https://kotlinlang.org/docs/characters.html)
- [Strings](https://kotlinlang.org/docs/strings.html)
- [Arrays](https://kotlinlang.org/docs/arrays.html)

## Nullable Variables

[Null Safety](https://kotlinlang.org/docs/null-safety.html)

Null point exception is the most commmon error in OOP languages. This usually occurs when you are trying to reference a null value.

For example:
```
var name: String = null;
```
The above statement will throw an error as 
`error: null can not be a value of a non-null type String.`
```
print(name.length)
```
 This will throw a null point exception
It can be prevented by using the following syntax that signifies the type of string as nullable.
```
var name: String? = null;
```

If we need to find the length of the variable, we can use the following syntax to avoid null point exception.

```
print(name?.length)
```
if the variable name is null it will return kotlin.Int as null if the string is present it will give the length of the string avoiding the null point exception.

## Condtional Statements

[Conditions and loops](https://kotlinlang.org/docs/control-flow.html)

In Kotlin `when` is similar to `switch` statement.

for example:

```
fun main(args: Array<String>) {
    var mode: Int = 4;
    when (mode) {
        1 -> println("value is ${mode} and is lazy");
        2 -> {
            println("value is ${mode} and is busy");
            println("Ok this is same as switch statements")
        }
        else -> println("value is ${mode} and is not supported")
    }
}
```

When statements can also be used to cehck for range values.

```
when (x) {
    in 1..10 -> print("x is in the range")
    in validNumbers -> print("x is valid")
    !in 10..20 -> print("x is outside the range")
    else -> print("none of the above")
}
```

## Arrays and Lists

[Arrays](https://kotlinlang.org/docs/arrays.html)

Arrays can be created using functions, such as arrayOf(), arrayOfNulls() or emptyArray().
Below are some examples on how to create arrays in Kotlin

```
fun main(args: Array<String>) {
    // immutable
    val array = arrayOf("Virginia", "Colorado", "Texas");
    // immutable
    val list = listOf("Orange", "Apple", "Banana");
    // mutable
    val arrayList = arrayListOf("Patrick", "Steward");
    arrayList.add("Sandra")
    // mutable
    val mutableList = mutableListOf("Cat", "Dog");
    mutableList.remove("Cat");
}
```

### Adding and removing elements

```
    val arrayList = arrayListOf("Patrick", "Steward");
    // inserting a new element at the end of the list
    arrayList.add("Sandra");
    println(arrayList.size);
    // inserting a new element at index 2
    arrayList.add(2, "Batman");
    println(arrayList);
    println(arrayList.size);
    // removing an element from the list this returns a boolean value
    val removed = arrayList.remove("Patrick");
    println(arrayList.size);
    println(removed);
```

### Naming loops

In Kotlin you can name the loops.

```
namedLoop@ for (i in 1..10) {
    for (j in 1..10) {
        break@namedLoop
    }
    println("$i $j");
}
```

### Qualified names vs unqualified names

in java/kotlin the qualified names are the methods that are called with the full package name.

for example `return java.util.Date()` is a qualified name.
where as `return Date()` is a unqualified name. To use unqualified names, the pacakge must be imported.
