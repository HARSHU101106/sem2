class Details:
    def stu_info(self):
        self.name=input("ENTER CANDIDATE NAME:")
        self.rollno=int(input("ENTER CANDIDATE ROLLNO:"))
        self.dep=input("ENTER CANDIDATE DEPARTMENT:")
    def display(self):
        print("NAME:",self.name,"\nROLLNO:",self.rollno,"\nDEPARTMENT:",self.dep)
class Courses:
    def stu_course(self):
        self.course=input("ENTER REGISTERED COURSE:")
    def disp(self):
        print("REGISTERED COURSE:",self.course)
class Registration(Details,Courses):
    def info(self):
        self.stu_info()
        self.stu_course()
    def display_details(self):
        print("REGISTERED CANDIDATE DETAILS:")
        self.display()
        self.disp()
obj=Registration()
obj.info()
obj.display_details()


