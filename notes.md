# OOP in python 
#### everything in python is objects
#### generality to specificity
#### 1.object   2.class 3.abstraction  4. inheritance 5. encapsulation  6.polymorphism
#### class
####  a=2 is a object of the integer  class 
####  datatype is the class 
#### making a class is time consuming 
#### class is a blueprint of how an object behave 
####  consists of data and functions
#### PascalCase, camelCase, snake_case
#### class in PascalCase and methods or fns in snake case thats the notation
![img.png](img.png)
#### python provides object literal for built in classes
#### Methods are functions written inside a class 
#### l.append is a method of list class and len(l) is a function as it doesnt belong to any class 
#### to declare variables inside a clas we need to define them inside a method __int__
#### to create your own methods that you can import you need to keep them inside the library foleder or python 
#### some methods are magic methods special methods dunder methods and constructor ias one of them 
[dunder methods ] (https://docs.python.org/3/reference/datamodel.html#special-method-names)
#### magic methods are called automatically we dont need to call them
#### we keep the configuration settings in the construvtor method like connecting to the internet which shouldnt have the control to user 
#### self is same thing as the object created i.e. hdfc 
#### when an method is called  then the default input is the object itself ...so self is provided 

## Encapsulation
#### Instance variables are the variables declared inside a constructor \
#### value is different for all objects 
#### access modifiers are words that u put before data like private public static etc
#### put __ before variable to make it private
#### nothing in python s truely private 
#### _Atm__pin ..is the var name after being calld by the object so we can modifyb thwe vardirectly

## refernce variable 
#### sbi is the refreence variable which stores the object created by sbi = Atm()
#### by pass by reference original value gets changed

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


#### sets can only have immutable data types 

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
#### if you are using some only static variables in a meyhod then name them static methods by ..@staticmethod before every method name 


## Agrregation 
![img_1.png](img_1.png)

#### aggregration has relationship ..inheritance ..is a relaationship