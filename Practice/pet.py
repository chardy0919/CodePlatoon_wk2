from abc import ABC, abstractmethod

class Pet(ABC):

    def __init__(self, name, color, breed, age):
        self.name = name
        self.color = color
        self.breed = breed
        self._age = age

    @property
    def get_age(self):
        return self._age
    
    @get_age.setter
    def set_age(self, new_age):
        if isinstance(new_age, int) and new_age > self._age:
            self._age = new_age
            
    def sleep(self):
        print(f"{self.name} is sleeping...Zzz")

    def play(self):
        print(f"{self.name} is playing")

    @abstractmethod
    def speak(self):
        pass