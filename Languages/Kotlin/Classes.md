# [Class in Kotlin](https://kotlinlang.org/docs/classes.html)

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

## [Inheritance](https://kotlinlang.org/docs/inheritance.html#overriding-methods)

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

## Overriding Rules

 - When overriding a property during inheritance, the method should begin with `override` keyword.
 - `final` keyword is used to make the methods protected. It will prevent the child properties from modifying the contents. (Encapsulation)
 The example below shows this in KotlinCourseChild() class.
 - When a child class in inheritating from multiple classes that share the same property name, the property must have overriden implementation in the child class.
 - `super` keyword can be used to access the properties of the parent class. If inheritating from multiple class, angle brackets <> can be used with parent class name, to access the method within the parent class. Example in KotlinCourseInheritance().

 ```
 interface Learnable {
    fun learn() {
        println("Learning")
    }
}

abstract class Course(val topic: String, val price: Double) {
    open fun learn() {
        println("Learning a $topic course");
    }
}

class KotlinCourse(): Course("Kotlin", 999.99) {
    override final fun learn() {
        println("One of the cool course is ${topic} and the price is ${price}");
        // Since this is inherited from a single class, super keyword can be used
        super.learn();
    }
}

class KotlinCourseChild(): KotlinCourse() {
    override fun learn() {
        println("One of the cool course is ${topic} and the price is ${price}");
        // Since this is inherited from a single class, super keyword can be used
        super.learn();
    }
}

class KotlinCourseInheritance(): Course("Kotlin", 999.99), Learnable {
    override fun learn() {
        // Since this is inherited from multiple classes, super keyword needs to be used with the classname.
        super<Course>.learn();
        super<Learnable>.learn();
    }
}

fun main(args: Array<String>) {
    val kotlinCourse = KotlinCourse();
    kotlinCourse.learn();

    val kotlinCourseInheritance = KotlinCourseInheritance();
    kotlinCourseInheritance.learn();
}
 ```

 ## [Data Classes](https://kotlinlang.org/docs/data-classes.html)

- Two objects of the data classes can be compared as a string.
- Allows destructuring of the objects.
- Allows user to copy and modify the contents of the data classes.

### Usecase of data classes

- Defining a useful string representation of the class'objects using toString().
- Implementing a useful equals() method that compares all the properties.
- Implementing a copy() method that allows us to easily make copies of a data object.
- Allowing us to use the data objects with data types that use hasing, such as HashSet.
- Decompose data objects into their properties.

 ```
 class Book(val title: String, val author: String, val releaseYear: Int, var price: Double) {
    override fun toString(): String {
        return "Book[title=$title, author=$author, releaseYear=$releaseYear, price=$price]"
    }
}

data class DataBook(val title: String, val author: String,val releaseYear: Int, var price: Double) {

}

fun main(args: Array<String>) {
    val book = Book("Kotlin", "John Doe", 2017, 1200.00);
    val book2 = Book("Kotlin", "John Doe", 2017, 1200.00);
    val dataBook = DataBook("Kotlin", "John Doe", 2017, 1200.00);
    val dataBook2 = DataBook("Kotlin", "John Doe", 2017, 1200.00);


    println(book);
    println(dataBook);

    // when comparing the objects for two classes, the string comparison for the objects of data classes returns correct
    // value
    println(book.equals(book2));  // false
    println(dataBook.equals(dataBook2));  // true

    // objects from data class can use the copy method and the property can be updated using the arguments
    val dataBook3 = dataBook2.copy(price = 90.00)
    println(dataBook3);

    // objects from the data class can be de-structured
    val (title, author) = dataBook;
    println("title -> $title ; author -> $author");

    // we can create hash set of the data objects. It will automatically remove the duplicate items from the hash
    val setData = hashSetOf(dataBook, dataBook2, dataBook3);
    println(setData);
}
 ```

 # [Singleton](https://kotlinlang.org/docs/object-declarations.html#object-declarations-overview)

 `object` keyword is used to create singleton classes. These are static and the properties are accessed using the class name.

 For example:

 ```
 // Declares a Singleton object to manage data providers
object DataProviderManager {
    private val providers = mutableListOf<DataProvider>()

    // Registers a new data provider
    fun registerDataProvider(provider: DataProvider) {
        providers.add(provider)
    }

    // Retrieves all registered data providers
    val allDataProviders: Collection<DataProvider> 
        get() = providers
}

// accessing the property of the singleton
DataProviderManager.registerDataProvider(exampleProvider)
 ```


