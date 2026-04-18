# Day 10: Object-Oriented Programming (OOPs)

## Topics Covered:
- OOP introduction
- Classes and Objects
- Attributes and Methods
- Constructor (__init__)
- Class vs Instance attributes
- Instance, Class and Static methods

## Key Learnings:
- Classes act as blueprints for objects
- Instance attributes belong to objects
- Class attributes are shared among objects
- Instance methods use 'self'
- Class methods use 'cls'
- Static methods are independent of class/object

## Example:

class Student:
    def __init__(self, name):
        self.name = name

## Why Important:
OOP helps in writing structured, reusable and scalable code.

## Learning Outcome:
- Able to create classes and objects
- Understand different types of methods
- Apply OOP concepts in real programs

## Encapsulation
- Data hiding using private variables (__)
- Access data using methods
- Improves security and control

### Inheritance

- Child class can inherit properties and methods from parent class
- Code reusability increases
- Method overriding allows different behavior

Example:
Dog and Cat inherit from Animal class

### Abstraction

- Hides implementation details
- Shows only essential features
- Achieved using abstract classes (ABC)

Example:
Shape is abstract class and Rectangle/Circle implement area()