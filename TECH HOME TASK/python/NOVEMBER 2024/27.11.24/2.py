'''' 2. Implement destructor and constructors using __del__() and __init__() to display student information.
Student information – name, age, course and grade'''
class Student:

    def __init__(self, name, age, course, grade):
        self.name = name
        self.age = age
        self.course = course
        self.grade = grade
    def __del__(self):
        print(f"Student Information for {self.name} has been deleted")
    def display_info(self):
        print(f"Student Information: \nName: {self.name}\nAge: {self.age}\nCourse: {self.course}\nGrade: {self.grade}")
student1 = Student("KRISH", 19 , "YOGA", "A")
student1.display_info()
del student1

        