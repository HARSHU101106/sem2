class Course:
    def __init__(self,name,duration,mode,price):
        self.name=name
        self.duration=duration
        self.mode=mode
        self.price=price
    def disp(self):
        print("DETAILS:","\nNAME:",self.name,"\nDURATION:",self.duration,"\nMODE:",self.mode,"\nPRICE:",self.price,"\n")
    def takencourse(self):
        self.person=input("ENTER THE NAME OF PERSON:")
        print(f"\n{self.person} took the course {self.name} for the price {self.price}\n")
    def durations(self):
        print(f"the duration of the course is {self.duration} and the mode is {self.mode}\n")
class FoundationofDS(Course):
    def takencourse(self):
        self.person=input("ENTER THE NAME OF PERSON:")
        print(f"\n{self.person} took the course {self.name} for the price {self.price}\n")
    def durations(self):
        print(f"the duration of the course is {self.duration} and the mode is {self.mode}\n")
obj1=FoundationofDS("Foundation level in DS","6 months","online","Rs.25000")
print("***********************************\n")
obj1.disp()
print("***********************************\n")
obj1.takencourse()
print("***********************************\n")
obj1.durations()
print("***********************************\n\n\n")
obj2=Course("Diploma level in DS","12 months","online","Rs.50000")
print("***********************************\n")
obj2.disp()
print("***********************************\n")
obj2.takencourse()
print("***********************************\n")
obj2.durations()
print("***********************************\n")
