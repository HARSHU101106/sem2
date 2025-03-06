class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
    
    def display_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Monthly Salary: ${self.salary}")
    
    def calculate_yearly_salary(self):
        return self.salary * 12


emp1 = Employee("HARSHINI", 270823, 10000)
emp1.display_info()
print(f"Yearly Salary: ${emp1.calculate_yearly_salary()}")
