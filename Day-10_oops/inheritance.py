# Day 10: Inheritance Example

# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")


# Child Class
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")


# Objects
d = Dog("Tommy")
c = Cat("Kitty")

d.speak()
c.speak()