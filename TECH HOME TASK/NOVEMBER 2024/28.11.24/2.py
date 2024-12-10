'''2. Write a Python program to demonstrate single inheritance. Create a parent class Employee with 
attributes name and salary, and a method display_details to show the employee's details. Create a 
child class Manager that inherits from Employee and adds an attribute department, along with a 
method display_department to show the department name. Create an object of the Manager class to 
display all details'''
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    def display_department(self):
        print(f"Department: {self.department}")
manager = Manager("KRISH",500000, "IT")
manager.display_details()
manager.display_department()

