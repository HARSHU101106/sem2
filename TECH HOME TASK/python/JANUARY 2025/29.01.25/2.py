class Customer: 
    def __init__(self, name, phone_number): 
        self.name = name 
        self.phone_number = phone_number 
 
    def display(self): 
        print("Customer Name:", self.name) 
        print("Customer Phone No.:", self.phone_number) 
 
 
class Depositor(Customer): 
    def __init__(self, name, phone_number, accno, balance): 
        super().__init__(name, phone_number) 
        self.accno = accno 
        self.balance = balance 
 
    def display(self): 
        super().display() 
        print("Customer A/C No.:", self.accno) 
        print("Balance:", self.balance) 
 
 
class Borrower(Depositor): 
    def __init__(self, name, phone_number, accno, balance, loan_no, 
loan_amt): 
        super().__init__(name, phone_number, accno, balance) 
        self.loan_no = loan_no 
        self.loan_amt = loan_amt 
 
    def display(self): 
        super().display() 
        print("Loan No:", self.loan_no) 
        print("Loan Amount:", self.loan_amt) 
        print("-" * 70) 
 
 
customers = [] 
n = int(input("Enter number of customer details you want to add: ")) 
 
for i in range(n): 
    print("\nEnter details for Customer", i + 1) 
    name = input("Enter Customer Name: ") 
    phone_number = input("Enter Customer Phone No.: ") 
    accno = input("Enter Customer A/C No.: ") 
    balance = float(input("Enter Balance: ")) 
    loan_no = input("Enter Loan Number: ") 
    loan_amt = float(input("Enter Loan Amount: ")) 
 
    customer = Borrower(name, phone_number, accno, balance, loan_no, 
loan_amt) 
    customers.append(customer) 
 
print("\n" + "*" * 70) 
for customer in customers: 
    customer.display() 