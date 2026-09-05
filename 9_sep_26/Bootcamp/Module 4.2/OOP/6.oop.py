class Student:
    def __init__(self, name):
        self.name = name 


s1 = Student("Alice")
print(s1.nmae)

del s1.name
print(s1.name)