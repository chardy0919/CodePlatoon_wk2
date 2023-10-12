from pet import Pet

class Cat(Pet):
    def __init__(self, name, color, breed, age, claws = True):
        super().__init__(name, color, breed, age)
        # self.name = name
        # self.color = color
        # self.breed = breed
        # self._age = age
        self._claws = claws

    @property
    def get_claws(self):
        return self._claws
    
    @get_claws.setter
    def set_claws(self, has_claws):
        if isinstance(has_claws, bool):
            self._claws = has_claws

    @property
    def get_age(self):
        return self._age
    
    @get_age.setter
    def set_age(self, new_age):
        if isinstance(new_age, int) and new_age > self._age:
            self._age = new_age
    
    def speak(self):
        print("Meow. Meow.")
    
    # def sleep(self):
    #     print(f"{self.name} is sleeping...Zzz")

    def play(self):
        print(f"{self.name} is playing with a string!")