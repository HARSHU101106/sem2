'''Create a Student class to manage basic student information.
1. Attributes:
➢ student_id: Unique identifier for the student in the format STU1234.
➢ name: The name of the student. ( Must be at least 2 characters long and should only 
contain alphabets and spaces.)
➢ grade: The grade/class of the student. (Should only accept specific valid grades, e.g., 
"1st Grade", "2nd Grade", ..., "12th Grade".Ensure the grade follows the format: 
<number>th Grade)
2. Methods:
➢ Validatedetails()
➢ display_details()'''
class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id 
        self.name = name
        self.grade = grade
        self.stu_id = False
        self.stu_name = False
        self.stu_grade = False
    def Validatedetails(self):
        if len(self.student_id) == 7 and self.student_id[:3] == "STU" and self.student_id[3:].isdigit():
            self.stu_id = True
        if len(self.name) >= 2 and all(char.isalpha() or char.isspace() for char in self.name):
            self.stu_name = True
        valid_grades = [f"{i}th Grade" for i in range(1, 13)]
        valid_grades[0] = "1st Grade"  
        if self.grade in valid_grades:
            self.stu_grade = True
    def display_details(self):
        if self.stu_id:
            print("STUDENT ID:", self.student_id, "IS VALID")
        else:
            print("STUDENT ID IS INVALID")
        if self.stu_name:
            print("STUDENT NAME:", self.name, "IS VALID")
        else:
            print("STUDENT NAME IS INVALID")
        if self.stu_grade:
            print("STUDENT GRADE:", self.grade, "IS VALID")
        else:
            print("STUDENT GRADE IS INVALID")
stu = Student("STU1234", "Harshini S", "2nd Grade")
stu.Validatedetails()
stu.display_details()
