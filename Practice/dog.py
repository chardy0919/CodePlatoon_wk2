from pet import Pet

class Dog(Pet): #child of Pet class
    def __init__(self, name, color, breed, age):
        super().__init__(name, color, breed, age)
    #     self.name = name
    #     self.color = color
    #     self.breed = breed
    #     self._age = age

    # @property
    # def get_age(self):
    #     return self._age
    
    # @get_age.setter
    # def set_age(self, new_age):
    #     if isinstance(new_age, int) and new_age > self._age:
    #         self._age = new_age
    
    def speak(self):
        print("WOOF! WOOF!")
    
    # def sleep(self):
    #     print(f"{self.name} is sleeping...Zzz")

    def play(self):
        print(f"{self.name} is playing with a bone!")
