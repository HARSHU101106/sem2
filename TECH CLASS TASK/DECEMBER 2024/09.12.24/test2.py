class Student:
    def __init__(self, name, rollno, dept, mark1, mark2, mark3, mark4, mark5):
        self.name = name
        self.rollno = rollno
        self.dept = dept
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
        self.mark4 = mark4
        self.mark5 = mark5
        self.total = mark1 + mark2 + mark3 + mark4 + mark5
    def display(self):
        print(f"NAME: {self.name}")
        print(f"ROLLNO: {self.rollno}")
        print(f"DEPARTMENT: {self.dept}")
        print(f"SUB1: {self.mark1}")
        print(f"SUB2: {self.mark2}")
        print(f"SUB3: {self.mark3}")
        print(f"SUB4: {self.mark4}")
        print(f"SUB5: {self.mark5}")
        print(f"TOTAL: {self.total}")
class Details(Student):
    def __init__(self, name, rollno, dept, mark1, mark2, mark3, mark4, mark5):
        super().__init__(name, rollno, dept, mark1, mark2, mark3, mark4, mark5)
        self.percentage = self.total / 500 * 100  
    def disp_stu_det(self):
        print("STUDENT DETAILS:\n")
        self.display() 
        print(f"PERCENTAGE: {self.percentage:.2f}%")
obj = Details("KRISH", 270823, "DEPARTMENT OF YOGA", 90, 90, 85, 90, 95)
obj.disp_stu_det()
