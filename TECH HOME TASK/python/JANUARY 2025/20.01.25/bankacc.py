class BankAccount:
    def __init__(self):
        self.__account_number = None
        self.__balance = 0.0
    def set_account(self, account_number, initial_balance=0.0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.__account_number = account_number
        self.__balance = initial_balance
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        print(f"Deposited: {amount}. New balance: {self.__balance}")
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount
        print(f"Withdrawn: {amount}. New balance: {self.__balance}")
    def add_interest(self, rate):
        if rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        interest = self.__balance * rate / 100
        self.__balance += interest
        print(f"Added interest: {interest}. New balance: {self.__balance}")
    def get_account_info(self):
        return {
            "Account Number": self.__account_number,
            "Balance": self.__balance
        }
if __name__ == "__main__":
    account = BankAccount()
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))
    account.set_account(account_number, initial_balance)

    while True:
        print("\nMenu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Add Interest")
        print("4. View Account Info")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            rate = float(input("Enter interest rate: "))
            account.add_interest(rate)
        elif choice == "4":
            print(account.get_account_info())
        elif choice == "5":
            print("Exiting. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")
