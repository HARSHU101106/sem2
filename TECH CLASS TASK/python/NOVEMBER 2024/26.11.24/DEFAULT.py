#default
class Bio:
    def __init__(self,name="KRISH",age=19,department="Bsc.Yoga"):
       self.name=name
       self.age=age
       self.depart=department
    def show(self):
       print("name:",self.name,"age:",self.age,"Department:",self.depart)
g= Bio()
g.show()
h=Bio("HARSHU",18,"Bsc.AI")
h.show()