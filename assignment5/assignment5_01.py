student_marks = {'Alice': 85, 'Mike': 70}

name = input("Enter the student's name: ").strip().capitalize()

if name in student_marks:
    print("{}'s marks: {}".format(name, student_marks[name]))
else:
    print("Student not found")