class Student:
    name = "Nana"
    nationality = "Ugandan"


    def __init__(self, age, religion):
        self.age = age
        self.religion = religion


student1 = Student(22, "Muslim")
print(student1.age)