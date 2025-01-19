# OOP in Python 
#### Everything in Python is an object
#### Generality to specificity
#### 1. Object  2. Class  3. Abstraction  4. Inheritance  5. Encapsulation  6. Polymorphism
#### Class
####  a = 2 is an object of the integer class 
####  Datatype is the class 
#### Making a class is time-consuming 
#### Class is a blueprint of how an object behaves 
#### Consists of data and functions
#### PascalCase, camelCase, snake_case
#### Class in PascalCase and methods or functions in snake_case, that's the notation
![img.png](img.png)
#### Python provides object literals for built-in classes
#### Methods are functions written inside a class 
#### l.append is a method of list class and len(l) is a function as it doesn't belong to any class 
#### To declare variables inside a class we need to define them inside a method __init__
#### To create your own methods that you can import, you need to keep them inside the library folder of Python 
#### Some methods are magic methods, special methods, dunder methods, and constructor is one of them 
[dunder methods](https://docs.python.org/3/reference/datamodel.html#special-method-names)
#### Magic methods are called automatically, we don't need to call them
#### We keep the configuration settings in the constructor method like connecting to the internet which shouldn't have the control to the user 
#### self is the same thing as the object created i.e. hdfc 
#### When a method is called, the default input is the object itself, so self is provided 

## Encapsulation
#### Instance variables are the variables declared inside a constructor
#### Value is different for all objects 
#### Access modifiers are words that you put before data like private, public, static, etc.
#### Put __ before a variable to make it private
#### Nothing in Python is truly private 
#### _Atm__pin is the variable name after being called by the object so we can modify the variable directly

## Reference Variable 
#### sbi is the reference variable which stores the object created by sbi = Atm()
#### By pass by reference, the original value gets changed

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

#### Sets can only have immutable data types 

### Static Variables in Python OOP

#### Definition:
- **Static Variables** (also known as class variables) are variables that are shared among all instances of a class. Unlike instance variables, which are unique to each instance, static variables have the same value for all instances of the class.

#### Characteristics:
- Static variables are defined within a class but outside of any instance methods.
- They are initialized when the class is first defined.
- They are accessed using the class name or an instance of the class.

#### Usage:
- Static variables are useful for storing values that should be consistent across all instances of a class.
- They can be accessed directly via the class or through an instance.

#### Example:

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
#### If you are using only static variables in a method, then name them static methods by using @staticmethod before every method name 

## Aggregation 
![img_1.png](img_1.png)

#### Aggregation has a relationship, inheritance is a relationship

Class -> 1. Data or property 
         2. Methods or behavior 

Class name should be in PascalCase

Variables or data should be in snake_case


data in a class is generally private 
methods in a class are public or private
private entitities are generally denoted by - =ve in class diagram and public stuff by + sign

l = [1,2,3] ->  object literal givem for built in classes 
l = list() -> normal defination of calling a method 

city = str()
