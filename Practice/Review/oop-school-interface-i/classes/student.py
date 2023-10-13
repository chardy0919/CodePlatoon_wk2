import csv
from classes.person import Person

class Student(Person):
    def __init__(self, name, age, role, school_id, password):
        super().__init__(name, age, password, role)
        self.school_id = school_id

    def __str__(self):
        return(f"""{self.name}
---------------
age: {self.age}
id:  {self.school_id}""")

    @classmethod
    def all_members(cls):
        students = []
        with open('./data/students.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                new_student = cls(**row)
                students.append(new_student)
        # print(students)
        return students
