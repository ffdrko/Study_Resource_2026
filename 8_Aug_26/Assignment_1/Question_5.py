# Asking student for their name, class and school name
student_name = input("Enter your name: ")
student_class = input("Enter your class: ")
student_school = input("Enter your school name: ")

# Displaying the student's ID card information
print("-" * 5, "Student ID Card", "-" * 5)

print(f"""Name: {student_name}

Class: {student_class}

School: {student_school}""")

print("-" * 30) # Printing a line of dashes to separate the ID card from other outputs