# Class in Kotlin

[Classes](https://kotlinlang.org/docs/classes.html)

In kotlin classes can be created using the `class` keyword. Below is the sample where we create a simple class called person.

```
import java.util.Calendar

class Person {
    var name: String = "John";
    var age: Int = 21;

    fun speak() {
        println("Hello World");
    }

    fun greet(name: String) {
        println("Greet $name!");
    }

    fun getYearOfBirth() = Calendar.getInstance().weekYear - age;
}

fun main(args: Array<String>) {
    var person = Person();
    person.speak();
    person.greet("Johnny Silverhand");
    println(person.name);
    println(person.age);
    println(person.getYearOfBirth());
}
```

## Creating class with parameters

```
import java.util.Calendar

class Person(val name: String, val age: Int) {

    fun speak() {
        println("Hello World");
    }

    fun greet(name: String) {
        println("Greet $name!");
    }

    fun getYearOfBirth() = Calendar.getInstance().weekYear - age;
}

fun main(args: Array<String>) {
    val person = Person("John", 21);
    person.speak();
    person.greet("Johnny Silverhand");
    println(person.name);
    println(person.age);
    println(person.getYearOfBirth());
}
```

## Inheritance

For a class to be inheriteted by other classes, the base class needs to include the open keyword. Anything that needs to be overwritten in the base class should be prefixed by the keyword `open`

```
import java.util.Calendar

open class Person(open val name: String,open val age: Int) {

    open fun speak() {
        println("Hello World");
    }

    fun greet(name: String) {
        println("Greet $name!");
    }

    fun getYearOfBirth() = Calendar.getInstance().weekYear - age;
}

class Student(override val name: String, override val age: Int) : Person(name, age){
    override fun speak() {
        println("Hello World from student");
    }
}
fun main(args: Array<String>) {
    val person = Person("John", 21);
    person.speak();
    person.greet("Johnny Silverhand");
    println(person.name);
    println(person.age);
    println(person.getYearOfBirth());

    val student = Student("Jane Doe", 18);
    student.speak();
    student.greet("Johnny Silverhand");
    println(student.name);
    println(student.age);
    println(student.getYearOfBirth());
}
```

## Abstract Classes

In Kotlin, you can create abstract classes by simply replacing the `open` keyword with abstract. The main difference between the class that is defined with abstract vs open is that the classes that are declared with abstract keyword cannon be instantiated but can be inheriteted.

If you try to create an object from the base/abstracted class, it will throw an error.

```
import java.util.Calendar

abstract class Person(open val name: String,open val age: Int) {

    abstract fun speak();

    fun greet(name: String) {
        println("Greet $name!");
    }

    fun getYearOfBirth() = Calendar.getInstance().weekYear - age;
}

class Student(override val name: String, override val age: Int) : Person(name, age){
    // if the speak method is not overriden, it will throw an error as abstract method needs to have implementation in the subclasses.
    override fun speak() {
        println("Hello World from student");
    }
}
fun main(args: Array<String>) {
//    val person = Person("John", 21);
//    person.speak();
//    person.greet("Johnny Silverhand");
//    println(person.name);
//    println(person.age);
//    println(person.getYearOfBirth());

    val student = Student("Jane Doe", 18);
    student.speak();
    student.greet("Johnny Silverhand");
    println(student.name);
    println(student.age);
    println(student.getYearOfBirth());
}
```

### Abstract vs Open

| Abstract| Open |
|---------|------|
|Requires the class to be inherited as it cannot be instantiated.| Can be instantiated independently while allowing inheritence.|
|When a property is declared with abstract keyword, it must be overwritten or implemented in the subclass. Subclass will not work if the abstract method is not implemented withing the subclass|When a property is declared with open keyword, it will not require the property to be overwritten as it will act as a default value. If needed the subclasses can overwrite the properties.|
| Abstract properties MUST be overriden in all (non-abstract) child classes |  Open properties and methods are ALLOWED to be overriden in all (non-abstract) child classes.|


## Interfaces

[Interface Docs](https://kotlinlang.org/docs/interfaces.html)

Interfaces define a contract that different classes may choose to follow. To do that, they have to override each method and property defined in the interface.

Interface provides the highest level of abstraction.

## Summary

- 