class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displayinfo(self):
        print("name:",self.name,"\nage:",self.age)
class employee(person):
    def __init__(self,name,age,id):
        super().__init__(name,age)
        self.id=id
    def displayemployee(self):
        super().displayinfo()
        print("id:",self.id)
class manager(employee):
    def __init__(self,name,age,id,salary):
        super().__init__(name,age,id)
        self.salary=salary
    def displaymanager(self):
        super().displayemployee()
        print("salary:",self.salary)
man=manager("KRISH",20,270823,5000000)
man.displaymanager()