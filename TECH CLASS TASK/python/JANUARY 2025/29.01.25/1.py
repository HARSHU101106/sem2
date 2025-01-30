class MaggiPack:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def validate_budget(self, budget):
        try:
            budget = float(budget)
            if budget < 0:
                raise ValueError("Budget cannot be negative.")
            return budget
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            return None
    
    def calculate_balance(self, budget):
        return budget - self.price
    
    def check_budget(self, budget):
        valid_budget = self.validate_budget(budget)
        if valid_budget is None:
            return
        
        if valid_budget >= self.price:
            balance = self.calculate_balance(valid_budget)
            print(f"You can buy {self.name} Maggi Pack")
            if balance == 0:
                print("It's complete")
            else:
                print(f"Here is your change {balance}")

maggi_sizes = [
    MaggiPack("Small", 20),
    MaggiPack("Regular", 50),
    MaggiPack("Big", 100)]
user_budget = float(input("What is your budget? "))
'''for maggi in maggi_sizes:
    maggi.check_budget(user_budget)'''
if user_budget>=100:
    maggi_sizes[2].check_budget(user_budget)
elif user_budget>20 and user_budget<=50:
    maggi_sizes[1].check_budget(user_budget)
elif user_budget>=20:
     maggi_sizes[0].check_budget(user_budget)

       