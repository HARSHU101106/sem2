#multiple inheritence
class Employee:
    def _init_(self,name,id,position):
        self.name=name
        self.id=id
        self.position=position
    def display_info(self):
        print(" Employee_name:",self.name,"\n","Employee_id:",self.id,"\n","Employee_position:",self.position)
class Address:
    def _init_(self,street,state,country):
        self.street=street
        self.state=state
        self.country=country
    def display(self):
        print(" Street_name:",self.street,"\n","State_name:",self.state,"\n","Country_name:",self.country)
class Employee_Details(Employee,Address):
    def _init_(self,name,id,position,street,state,country):
        super(). _init_(name,id,position)
        Address._init_(self,street,state,country)
    def dis(self):
        self.display_info()
        self.display()
e=Employee_Details(" Priya",46765,"Manager","Gandhi_nagar","Tamilnadu","India")
e.dis()#multiple inheritence
class Employee:
    def _init_(self,name,id,position):
        self.name=name
        self.id=id
        self.position=position
    def display_info(self):
        print(" Employee_name:",self.name,"\n","Employee_id:",self.id,"\n","Employee_position:",self.position)
class Address:
    def _init_(self,street,state,country):
        self.street=street
        self.state=state
        self.country=country
    def display(self):
        print(" Street_name:",self.street,"\n","State_name:",self.state,"\n","Country_name:",self.country)
class Employee_Details(Employee,Address):
    def _init_(self,name,id,position,street,state,country):
        super(). _init_(name,id,position)
        Address._init_(self,street,state,country)
    def dis(self):
        self.display_info()
        self.display()
e=Employee_Details(" Priya",46765,"Manager","Gandhi_nagar","Tamilnadu","India")
e.dis()