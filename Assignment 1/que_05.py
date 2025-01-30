"""You are a student in a class of 10. Your class teacher assigns you a task of entering the
names of all the students in the class. You finally want to display the names given the
condition that the maximum allowed characters in a name is 15. As a fun task, reverse the
names and display them. [Hint: Slicing works when you are selecting maximum characters]"""

students_name = []
students = int(input("Enter the number of students: "))

for i in range(students):
    name = input(f"Enter the name of student {i + 1}: ")
    students_name.append(name[:15])

print("\nOriginal Names:")
for student in students_name:
    print(student)

print("\nReversed Names:")
for student in students_name:
    print(student[::-1])