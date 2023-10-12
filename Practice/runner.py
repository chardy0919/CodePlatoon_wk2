from intro_python_OOP import Student
from dog import Dog
from cat import Cat

student_one = Student("Joe", "joe@student.org")
student_two = Student("Cody", "cody@student.org")
student_three = Student("Bob", "bob@student.org")
# def create_a_student():
#     name = input("Students name?  ")
#     email = name+"@student.org"
#     new_student = Student(name,email)
#     print(Student.all_students)

# create_a_student()

#Student.add_a_student()

# Student.view_all_students()

molly = Dog("Molly", "Brown", "Dobrador", 3)
molly.speak()

sassy = Cat("Sassy", "black", "tuxedo", 9, False)
sassy.speak()