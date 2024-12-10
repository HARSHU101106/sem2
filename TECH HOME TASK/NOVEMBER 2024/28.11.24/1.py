'''1. Write a Python program that demonstrates single inheritance. Create a parent class called Person with 
an attribute name and a method show_name to display the name. Create a child class called Student
that inherits from the Person class and adds a new attribute student_id with a method 
show_student_id to display the student ID. Create an object of the Student class, and use it to display 
both the name and student ID.'''
class person:
    def name(self):
        self.names=input()
    def show_name(self):
        print("name : ",self.names)
class student(person):
    def stuid(self):
        self.stu_id=int(input())
    def show_stuid(self): 
        print("student id : ",self.stu_id)
g=student()
g.name()
g.stuid()
g.show_name()
g.show_stuid()