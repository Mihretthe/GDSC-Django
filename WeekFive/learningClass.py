
"""
self : we use self as a naming convention we can use any word for that.
"""


class Person:
    def __init__(self, name = "Mihret", age = 21) -> None:
        self.name = name
        self.age = 21

    def greeting(self)-> None:
        # return "Hello" +" "+ self.name
        return f"Hello {self.name}"


person = Person(name = "Fasik")
person2 = Person()
print(person.greeting())
print(person2.greeting())
        


class Rectangle:
    def __init__(self, length, width):
        self.__name = length
        self.length = length
        self.width = width
        print("Rectangle Created")

    def calculateArea(self):
        return self.length * self.width
    
    def calculatePerimeter(self):
        return 2 * (self.length + self.width)
    
rectangle1 = Rectangle(5,6)

# print(rectangle1.calculateArea())
# print(rectangle1.calculatePerimeter())
        

# Encapsulation

# Hiding the things that the users should not access.

# Inheritance

# Parent child relationship

# Abstraction

# A class that inherits ABC from abc that have at least one abstract method

# Polymorphism 

# Static (compile-time) Polymorphism and Dynamic (run-time) Polymorphism

class Dog:
    def __init__(self, name = 'Bobi'):
        self.name = name

    def canMove(self):
        return f"{self.name} can run fast"
    
    def canEat(self):
        return f"{self.name} loves bone"
    
    def canBark(self):
        
        return "Bark Bark"
    
dog = Dog()

# print(dog.canBark())
# print(dog.canMove())
# print(dog.canEat())

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color
    
    @abstractmethod    
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.color = "Blue"

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.color = "Red"

    def area(self):
        return self.radius * pi * self.radius


circle = Circle(2)
print(circle.get_color(), circle.area())

rectangle = Rectangle(3,4)
print(rectangle.get_color(), rectangle.area())

# Read about super