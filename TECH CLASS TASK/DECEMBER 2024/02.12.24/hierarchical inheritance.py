class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def displaystudent(self):
        print("NAME:",self.name,"\nROLLNO:",self.rollno)
class studetails(student):
    def __init__(self,name,rollno,dep,clg):
        super().__init__(name,rollno)
        self.dep=dep
        self.clg=clg
    def displaydet(self):
        super().displaystudent()
        print("DEPARTMENT:",self.dep,"\nCOLLEGE:",self.clg,"\n")
class stuscores(student):
    def __init__(self,name,rollno,marks,rank):
        super().__init__(name,rollno)
        self.marks=marks
        self.rank=rank
    def displaystuscores(self):
        super().displaystudent()
        print("MARKS:",self.marks,"\nRANK:",self.rank)
g=studetails("KRISH",270823,"Bsc.Yoga","TAMIL NADU SPORTS UNIVERSITY")
g.displaydet()
h=stuscores("KRISH",270823,450,2)
h.displaystuscores()