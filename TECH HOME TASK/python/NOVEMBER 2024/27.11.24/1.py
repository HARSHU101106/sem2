'''1. Given students details, marks in 5 subjects and we have to find student's grade.
In this program, you have to take student name, roll number and marks in 3 subjects and calculating 
student's grade based on the percentage and printing the all details.
Calculate Student's Grade
To calculate a student's grade using a Python program, you can simply input the student's details like 
roll number, name, and marks in specified subjects. And, based on the given marks in the subjects, 
you can calculate the percentage and find and print the grade as per the below-given conditions:
• If the percentage is >=85, then the grade will be "S".
• If the percentage is >=75, then the grade will be "A".
• If the percentage is >=65, then the grade will be "B".
• If the percentage is >=55, then the grade will be "C".
• If the percentage is >=50, then the grade will be "D".'''
class student:
    def __init__(self,name,rollno,sub1,sub2,sub3,):
        self.name=name
        self.rollno=rollno
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
        self.per=((sub1+sub2+sub3)/3)*100
    def grade(self):
        if self.per >=85: 
           print("grade is S")
        elif self.per >=75: 
            print("grade is A")
        elif self.per >=65: 
            print("grade is B")
        elif self.per >=55: 
            print("grade is C")
        elif self.per >=50: 
            print("grade is D")
        else:
            print("SORRY, NO GRADE AVAILABLE")

obj=student("KRISH",270823,90,95,100)
obj.grade()        
