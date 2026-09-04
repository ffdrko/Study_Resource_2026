class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avarage_marks(self):
        return sum(self.marks) / len(self.marks)



student1 = Student("Fahim", [85, 75 , 90])

student1_average_marks = student1.avarage_marks()
print(f"{student1_average_marks:.2f}")