class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks  
    
    def average_marks(self):
        return (sum(self.marks.values()) / 300)*100

class StudentRecords(Student):
    def __init__(self):
        self.students = []
    
    def add_student(self, name, roll_no, marks):
        student = Student(name, roll_no, marks)
        self.students.append(student)
    
    def find_topper(self):
        if not self.students:
            return None
        topper = max(self.students, key=lambda student: student.average_marks())
        return topper

records = StudentRecords()
records.add_student("HARSHINI", 101106, {"SUB1": 90, "SUB2": 90, "SUB3": 90})
records.add_student("KRISHNA", 210005, {"SUB1": 100, "SUB2": 85, "SUB3": 90})


topper = records.find_topper()
if topper:
    print(f"Topper: {topper.name}, Roll No: {topper.roll_no}, Average Marks: {topper.average_marks():.2f}")

