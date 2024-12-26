class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New Balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}. New Balance: {self.balance}")
    def check_balance(self):
        print(f"Current Balance: {self.balance}")
account = BankAccount("KRISHNA", 1000)
account.check_balance()
account.deposit(500)
account.withdraw(300)
account.withdraw(1500)
