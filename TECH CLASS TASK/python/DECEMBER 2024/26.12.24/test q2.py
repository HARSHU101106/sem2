class Student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def finderror(self):
        char=False
        for i in self.name:
            if i.isalpha():
                char=True
            else:
                char=False
                break
        if char==False:
            raise ValueError("Invalid Name")
        if self.mark<0 or self.mark>100:
            raise ValueError("Invalid Marks")
    def grade(self):
        if self.mark>=90 and self.mark<=100:
            return "GRADE A"
        elif self.mark>=80 and self.mark<=89:
            return "GRADE B"
        elif self.mark>=70 and self.mark<=79:
            return "GRADE C"
        elif self.mark>=60 and self.mark<=69:
            return "GRADE D"
        elif self.mark<60:
            return "GRADE E"
name=input()
mark=int(input())
a=Student(name,mark)
try:
    a.finderror()
    print(a.grade())
except ValueError as e:
    print(e)