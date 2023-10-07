class User:
    def __init__(self, name, email, age):
        self._name = name
        self._email = email
        self._age = age

    @property
    def get_name(self):
        return self._name
    @property
    def get_email(self):
        return self._email
    @property
    def get_age(self):
        return self._age
    
    @get_name.setter
    def set_name(self,new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            print("Not a string")

    @get_email.setter
    def set_email(self, new_email):
        if isinstance(new_email, str):
            self._email = new_email
        else:
            print('Invalid email')
    
    @get_age.setter
    def set_age(self, new_age):
        if isinstance(new_age, int) and new_age == 69:
            print('Nice...')
            self.age = new_age
        elif isinstance(new_age, int) and new_age > 0:
            self.age = new_age
        else:
            print('Invalid age')
    
user_1 = User('Bill', "billseeker@gmail.com", 55)
print(user_1.get_name)
user_1.set_name="Pill"
print(user_1.get_name)