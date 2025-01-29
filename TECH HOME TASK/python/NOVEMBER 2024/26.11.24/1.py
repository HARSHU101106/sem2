'''1. Create a BankAccount class that handles common operations like depositing money, 
withdrawing money, and checking the balance.
For each bank account, variables to be maintained are:
1. Account Holder's Name
2. Account Number
3. Balance
The class will allow the following actions(methods):
1. Deposit Money – pass parameter “amount” to call deposit method
2. Withdraw Money - pass parameter “amount” to call withdraw method
3. Check Balance
Note : Use parameterised constructor'''
class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: {amount}. New balance: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")
    def check_balance(self):
        print(f"Current balance: {self.balance}")
        return self.balance
account = BankAccount("KRISH", "27082023", 5000000)
account.check_balance()
account.deposit(101106)    
account.withdraw(21005)
account.check_balance()
