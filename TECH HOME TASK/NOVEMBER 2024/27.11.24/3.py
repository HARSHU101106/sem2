class employee:
    def getemp(self):
        self.id=input("enter id:")
        self.name=input("enter name:")
    def displayemp(self):
        print("id=",self.id,"\n name=",self.name)
class perks(employee):
    def getdet(self):
        self.getemp()
        self.sal=int(input("enter salary"))
    def displaydet(self):
        self.displayemp()
        print("salary=",self.sal)
p=perks()
p.getdet( )
p.displaydet()