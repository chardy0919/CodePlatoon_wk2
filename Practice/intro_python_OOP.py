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
    def __init__(self, name, breed, color, sound):
        self.name = name
        self.breed = breed
        self.color = color
        self.sound = sound
    
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

print(person.get_name)
person.set_name = "Bob"
print(person.get_name)