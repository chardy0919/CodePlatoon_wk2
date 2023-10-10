# Five Pillars of OOP:

# Encapsulation = Data access can be restricted based on needs
# Abstraction = Logic/Complexity is hidden, for simplicity
# Inheritance = Sharing of similar features and attributes (Is-a)
# Composition = Including other Objects as attributes (Has-a)
# Polymorphism = Objects can take different forms depending on needs/situation

# def scope_test():
#     def do_local():
#         spam = "local spam"

#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"

#     def do_global():
#         global spam
#         spam = "global spam"

#     spam = "test spam"
#     do_local()
#     print("After local assignment:", spam)
#     do_nonlocal()
#     print("After nonlocal assignment:", spam)
#     do_global()
#     print("After global assignment:", spam)

# scope_test()
# print("In global scope:", spam)

# def myfunc1():
#   x = "John"
#   def myfunc2():
#     nonlocal x
#     x = "hello"
#   myfunc2()
#   return x

# print(myfunc1())

class Dog:
    species = "Canis Lupus Familiaris"   # all dogs have the same species type => *class attribute*
    def __init__(self, name, breed, color, sound):
        self.name = name #These are all instance attributes
        self.breed = breed #These are all instance attributes
        self.color = color #These are all instance attributes
        self.sound = sound #These are all instance attributes
    
    def __str__(self):
        return f"I am a {self.color} {self.breed} dog named {self.name} and I say '{self.sound}'"
    
    def speak(self):
        print(f">> {self.sound}")
    
    def fetch(self, item):
        print(f">> {self.name} gonna go fetch the {item}")

Molly = Dog("Molly", "Dobrador", "Brown", "Moo")
# print(Molly.name)
# Molly.speak()
# Molly.fetch('refridgerator')
# print(Molly.species)


def my_decorator(func):
    def wrapper():
        print("Something happening before the function is called")
        func() #function then happens
        print("Something after the function is called")
    return wrapper

@my_decorator
def say_hello():
    print("hello")

@my_decorator
def molly():
    print(Molly)

# say_hello()
# molly()

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def get_name(self):
        return self._name
    
    @get_name.setter
    def set_name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            print("Name must be a string")
    
    @property
    def get_age(self):
        return self._age
    
    @get_age.setter
    def set_age(self, new_age):
        if isinstance(new_age, int) and new_age > 0:
            self._age = new_age
        else:
            print("Age must be a positive integer")

person = Person("Alice", 25)

# print(person.get_name)
# person.set_name = "Bob"
# print(person.get_name)

# Instance Methods
# Purpose and Use: Instance methods are the workhorses of OOP. They operate on the specific instance they are called on, allowing objects to perform actions and interact with their own attributes.

# Best Practices:

# Encapsulation: Use instance methods to encapsulate behaviors that directly manipulate or interact with instance attributes. This promotes data integrity and encapsulation by keeping data and behavior together.
# Customization: Instance methods enable customization of behavior for each instance. This is useful when different instances of a class need to perform the same action in a slightly different way.
# Example:

# calculate_area() in a Circle class calculates the area based on the radius attribute of the specific circle instance.
class Circle:
    pi = 3.14159
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self): #This is an instance method
        return self.pi * self.radius **2

circle = Circle(5)
# print(circle.calculate_area()) #78.53975

# Class Methods
# Purpose and Use: Class methods operate on the class itself rather than on instances. They can be used for class-level operations or to create alternative constructors.

# Best Practices:

# Class-Level Operations: Use class methods when the operation is related to the class as a whole and doesn't involve instance-specific data. These methods can be used to modify class attributes, perform calculations based on class-level information, or manage class-wide settings.
# Alternative Constructors: Class methods are often used to create alternative constructors that allow for different ways of initializing objects.
# Example:

# create_square() in a Rectangle class creates a square instance by using the class itself as a constructor.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @classmethod #specific decorator
    def create_square(cls, side_length): #This is a class method
        return cls(side_length, side_length)
    
square = Rectangle.create_square(4)
# print(square.width, square.height)

# Static Methods
# Purpose and Use: Static methods are independent of class and instance state. They're used to define utility functions that are related to the class but don't need access to instance-specific data.

# Best Practices:

# Code Organization: Use static methods to keep utility functions within the class's scope. This enhances code organization by associating relevant functions with the class they are related to.
# Enhanced Readability: Static methods provide clear visual cues that a function is related to a class without needing access to instance attributes.
# Example:

# is_palindrome() in a StringUtils class checks if a given string is a palindrome without needing any instance or class attributes.
class StringUtils:
    @staticmethod#specific decorator
    def is_palindrome(text): #This is a static method
        clean_text = text.replace(" ", "").lower()
        return clean_text == clean_text[::-1]
    
# print(StringUtils.is_palindrome("racecar")) #true