# OOP in Python 

## General Concepts
- Everything in Python is an object
- Generality to specificity
  1. Object
  2. Class
  3. Abstraction
  4. Inheritance
  5. Encapsulation
  6. Polymorphism

## Class and Object
- **Class**: 
  - `a = 2` is an object of the integer class.
  - Datatype is the class.
  - Making a class is time-consuming.
  - Class is a blueprint of how an object behaves.
  - Consists of data and functions.
  - PascalCase, camelCase, snake_case.
  - Class in PascalCase and methods or functions in snake_case, that's the notation.
  - ![img.png](img.png)
  - Python provides object literals for built-in classes.
  - Methods are functions written inside a class.
  - `l.append` is a method of list class and `len(l)` is a function as it doesn't belong to any class.
  - To declare variables inside a class we need to define them inside a method `__init__`.
  - To create your own methods that you can import, you need to keep them inside the library folder of Python.
  - Some methods are magic methods, special methods, dunder methods, and constructor is one of them.
  - [dunder methods](https://docs.python.org/3/reference/datamodel.html#special-method-names)
  - Magic methods are called automatically, we don't need to call them.
  - We keep the configuration settings in the constructor method like connecting to the internet which shouldn't have the control to the user.
  - `self` is the same thing as the object created i.e. `hdfc`.
  - When a method is called, the default input is the object itself, so `self` is provided.

### Example
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, my name is {self.name} and I am {self.age} years old."

# Creating objects
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Accessing properties and methods
print(person1.introduce())  # Output: Hi, my name is Alice and I am 25 years old.
print(person2.introduce())  # Output: Hi, my name is Bob and I am 30 years old.
```

## Encapsulation
- Instance variables are the variables declared inside a constructor.
- Value is different for all objects.
- Access modifiers are words that you put before data like private, public, static, etc.
- Put `__` before a variable to make it private.
- Nothing in Python is truly private.
- `_Atm__pin` is the variable name after being called by the object so we can modify the variable directly.

### Example
```python
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance

    def get_balance(self):  # Getter method
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn {amount}. Remaining balance is {self.__balance}.")
        else:
            print("Invalid withdrawal amount.")

# Example usage
account = BankAccount("12345", 1000)
account.deposit(500)
account.withdraw(300)
print(account.get_balance())  # Output: 1200
```

## Inheritance
- Inheritance allows a class (child) to acquire the properties and methods of another class (parent).

### Example
```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"{self.brand} {self.model}"

class Car(Vehicle):  # Inherits from Vehicle
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)  # Call parent constructor
        self.doors = doors

    def display_info(self):
        return f"{super().display_info()} with {self.doors} doors."

# Example usage
car = Car("Toyota", "Corolla", 4)
print(car.display_info())  # Output: Toyota Corolla with 4 doors.
```

## Polymorphism
- Polymorphism allows objects to take multiple forms, enabling methods to behave differently based on the object invoking them.

### Example
```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Example usage
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(f"Area: {shape.area()}")
```

## Abstraction
- Abstraction is the process of hiding implementation details and exposing only essential features.

### Example
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Example usage
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.sound())
```

## Association, Aggregation, and Composition
- **Association**: A general relationship between two classes.
- **Aggregation**: A weak relationship where the child can exist independently of the parent.
- **Composition**: A strong relationship where the child cannot exist without the parent.

### Example
```python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  # Aggregation

class Wheel:
    def __init__(self, size):
        self.size = size

class Vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels  # Composition

# Aggregation example
engine = Engine(150)
car = Car("Honda", engine)
print(f"{car.brand} car with {car.engine.horsepower} HP engine.")

# Composition example
wheels = [Wheel(16) for _ in range(4)]
vehicle = Vehicle("Toyota", wheels)
print(f"{vehicle.brand} vehicle with {len(vehicle.wheels)} wheels.")
```

## Reference Variable 
- `sbi` is the reference variable which stores the object created by `sbi = Atm()`.
- By pass by reference, the original value gets changed.

### Python's Behavior

- **Immutable Types**:
  - Types such as integers, strings, and tuples are immutable. When you pass an immutable object to a function, it behaves as if it is passed by value. 
  - You cannot change the original object itself; you can only reassign the reference to a new object. Therefore, changes inside the function do not affect the original object.
  
  **Example:**

  ```python
  def modify_value(x):
      x = x + 10  # This reassigns x to a new integer object

  num = 5
  modify_value(num)
  print(num)  # Output will still be 5
  ```

- Sets can only have immutable data types.

## Static Variables in Python OOP

### Definition:
- **Static Variables** (also known as class variables) are variables that are shared among all instances of a class. Unlike instance variables, which are unique to each instance, static variables have the same value for all instances of the class.

### Characteristics:
- Static variables are defined within a class but outside of any instance methods.
- They are initialized when the class is first defined.
- They are accessed using the class name or an instance of the class.

### Usage:
- Static variables are useful for storing values that should be consistent across all instances of a class.
- They can be accessed directly via the class or through an instance.

### Example
```python
class Counter:
    count = 0  # Static variable

    def __init__(self):
        Counter.count += 1  # Increment the static variable

    def display_count(self):
        print(f"Count: {Counter.count}")

# Creating instances of Counter
c1 = Counter()
c2 = Counter()
c3 = Counter()

# Displaying the count using instances
c1.display_count()  # Output: Count: 3
c2.display_count()  # Output: Count: 3

# Accessing the static variable directly from the class
print(Counter.count)  # Output: 3
```
- If you are using only static variables in a method, then name them static methods by using `@staticmethod` before every method name.

## Difference Between Method and Function

| Feature            | Method                                                                 | Function                                      |
|--------------------|------------------------------------------------------------------------|-----------------------------------------------|
| Definition         | A function that is defined inside a class and is associated with an object. | A block of code that performs a specific task and is not necessarily associated with an object. |
| Invocation         | Called on an object using the dot notation (e.g., `object.method()`).  | Called independently using its name (e.g., `function()`). |
| Binding            | Implicitly bound to an instance of the class (the `self` parameter).   | Not bound to any instance or class.           |
| Context            | Operates on data contained within the class instance.                 | Operates on data passed to it as parameters.  |
| Example            | ```python                         class MyClass:                     def my_method(self):                         print("This is a method")                     obj = MyClass()                     obj.my_method()                     ``` | ```python                     def my_function():                         print("This is a function")                     my_function()                     ``` |

## Aggregation 
![img_1.png](img_1.png)

- Aggregation has a relationship, inheritance is a relationship.

Class -> 
1. Data or property 
2. Methods or behavior 

- Class name should be in PascalCase.
- Variables or data should be in snake_case.
- Data in a class is generally private.
- Methods in a class are public or private.
- Private entities are generally denoted by `-` in class diagram and public stuff by `+` sign.

```python
l = [1,2,3]  # object literal given for built-in classes 
l = list()  # normal definition of calling a method 

city = str()
```

- Yes, public methods can be divided into static and non-static methods. Both static and non-static methods are accessible from outside the class, while private methods are not accessible directly from outside the class, regardless of whether they are static or non-static.

### Summary:
- **Public Methods**: Accessible from outside the class.
- **Static Methods**: Do not require an instance of the class to be called. Defined using the `@staticmethod` decorator.
- **Non-static Methods**: Require an instance of the class to be called. Defined normally with `self` as the first parameter.
- **Private Methods**: Not accessible directly from outside the class. Prefixed with a double underscore (`__`).

### Example
```python
class ATM:
    def __init__(self):
        self.__pin = None

    # Public non-static method
    def create_pin(self):
        temp = input('Enter your new PIN: ')
        self.__pin = temp
        print('PIN set successfully')
        self.__menu()  # Calling private method

    # Private method
    def __menu(self):
        print("Displaying menu")

    # Public static method
    @staticmethod
    def static_method_example():
        print("This is a static method")

    # Public non-static method
    def non_static_method_example(self):
        print("This is a non-static method")

# Example usage
atm = ATM()
atm.create_pin()  # Public non-static method
ATM.static_method_example()  # Public static method
atm.non_static_method_example()  # Public non-static method

# Trying to call the private method directly will raise an AttributeError
# atm.__menu()  # Uncommenting this line will raise an error
```






string formatting :

1. str.format()

name = "Alice"
age = 30
formatted_string = "Name: {}, Age: {}".format(name, age)
print(formatted_string)  # Output: Name: Alice, Age: 30

# With positional and keyword arguments
formatted_string = "Name: {0}, Age: {1}".format(name, age)
print(formatted_string)  # Output: Name: Alice, Age: 30

formatted_string = "Name: {name}, Age: {age}".format(name=name, age=age)
print(formatted_string)  # Output: Name: Alice, Age: 30


2.by  % operator
name = "Alice"
age = 30
formatted_string = "Name: %s, Age: %d" % (name, age)
print(formatted_string)  # Output: Name: Alice, Age: 30

