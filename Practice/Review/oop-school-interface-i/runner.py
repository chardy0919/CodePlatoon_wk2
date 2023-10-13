from classes.school import School 

school = School('Ridgemont High') 

while True: 

    mode = input("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")

    if mode == '5':
        print("Goodbye")
        break
    elif mode == '1':
        school.list_students()
    elif mode == '2':
        student_id = input('Enter student id:\n')
        student = school.find_student_by_id(student_id)
        if student:
            print(student)
    elif mode == '3':
        student_data = {'role':'student'}
        student_data['name']      = input('Enter student name:\n')
        student_data['age']       = input('Enter student age: \n')
        student_data['school_id'] = input('Enter student school id: \n')
        student_data['password']  = input('Enter student password: \n')
        school.add_student(student_data) 
    elif mode == '4':
        student_id = input('Enter student id:\n')
        student = school.find_student_by_id(student_id)
        if student:
            school.students.remove(student)
            print("Student was deleted.")
    else:
        pass 