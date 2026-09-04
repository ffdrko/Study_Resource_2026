class Student:
    def __init__(self, name, marks):
        # print("adding new student")
        self.name = name
        self.marks = marks

    def hello(self):
        print(f"Hello, {self.name}")

    def get_marks(self):
        return self.marks

student1 = Student("Karan", 85)
student2 = Student("Fahim", 90)

student1.hello()
student1_marks = student1.get_marks()
print(student1_marks)