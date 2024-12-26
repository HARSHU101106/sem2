#3.   
class Student:
    def _init_(self, name, age, marks):
        self.set_name(name)
        self.set_age(age)
        self.set_marks(marks)

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_age(self, age):
        if age < 5 or age > 100:
            raise ValueError("Age must be between 5 and 100.")
        self._age = age

    def get_age(self):
        return self._age

    def set_marks(self, marks):
        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100.")
        self._marks = marks

    def get_marks(self):
        return self._marks

student = Student("Alice", 20, 85)
student.set_age(21)
print(student.get_marks())