# Day 10: OOPs in Python

# -------- CLASS & OBJECT --------

class Student:
    school = "ABC School"   # class attribute

    def __init__(self, name, age):
        self.name = name    # instance attribute
        self.age = age

    def display(self):      # instance method
        print("Name:", self.name)
        print("Age:", self.age)


# Object
s1 = Student("Ankush", 20)
s1.display()


# -------- CLASS METHOD --------

class Demo:
    count = 0

    def __init__(self):
        Demo.count += 1

    @classmethod
    def show_count(cls):
        print("Total objects:", cls.count)


d1 = Demo()
d2 = Demo()
Demo.show_count()


# -------- STATIC METHOD --------

class Math:
    @staticmethod
    def add(a, b):
        return a + b
print("Sum:", Math.add(5, 3))


# -------- ENCAPSULATION --------

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


acc = BankAccount(1000)
acc.deposit(500)
print("Balance:", acc.get_balance())