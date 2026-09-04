class Student:
    def __init__(self, name, marks):
        print("adding new student")
        self.name = name
        self.marks = marks

student1 = Student("Karan", 85)
student2 = Student("Fahim", 90)

print(student1.name, student1.marks)
print(student2.name, student2.marks)
