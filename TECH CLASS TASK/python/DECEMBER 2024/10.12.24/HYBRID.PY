class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)
    
    def displayEmployeeInfo(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Manager(Employee):
    def __init__(self, name, age, eid):
        super().__init__(name, age)
        self.eid = eid
    
    def displayManagerInfo(self):
        self.displayEmployeeInfo()
        print("ID:", self.eid)

class Developer(Employee):
    def __init__(self, name, age, dept):
        super().__init__(name, age)
        self.dept = dept
    
    def displayDeveloperInfo(self):
        self.displayEmployeeInfo()
        print("Department:", self.dept)

class TeamLeader(Manager, Developer):
    def __init__(self, name, age, eid, dept, teamsize):
        Employee.__init__(self,name,age)
        self.eid=eid
        self.dept = dept
        self.teamsize = int(teamsize)
    
    def displayTeamLeaderInfo(self):
        self.displayManagerInfo()
        print("Department:", self.dept)
        print("Team Size:", self.teamsize)

 name = input("Enter name: ")
age = input("Enter age: ")
eid = input("Enter employee ID: ")
dept = input("Enter department: ")
teamsize = input("Enter team size: ")

obj = TeamLeader(name, age, eid, dept, teamsize)
obj.displayTeamLeaderInfo()
