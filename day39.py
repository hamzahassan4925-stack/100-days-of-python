class Student:
    name = "hassan babar"
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in the list")

s1 = Student("hassan babar")
print(s1.name)
