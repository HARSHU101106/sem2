class PizzaSize:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def validate_budget(self, budget):
        try:
            budget = float(budget)
            if budget < 0:
                raise ValueError("Budget cannot be negative")
            return budget
        except ValueError as e:
            print(e)
            return None

    def calculate_balance(self, budget):
        return budget - self.price

    def purchase_pizza(self, budget):
        valid_budget = self.validate_budget(budget)
        if valid_budget is None:
            return
        
        balance = self.calculate_balance(valid_budget)
        if balance >= 0:
            print(f"You can buy a {self.name} pizza.")
            if balance == 0:
                print("It's complete!")
            else:
                print(f"Here is your balance: {balance}")
        else:
            print(f"Sorry, you don't have enough money for a {self.name} pizza.")
pizzas = [
    PizzaSize("small", 100),
    PizzaSize("medium", 200),
    PizzaSize("large", 300)]
try:
    user_budget = float(input("What's your budget? "))
except ValueError:
    print("Invalid input! Please enter a valid number.")
    exit()
if user_budget >= 300:
    pizzas[2].purchase_pizza(user_budget)
elif user_budget >= 200:
    pizzas[1].purchase_pizza(user_budget)
elif user_budget >= 100:
    pizzas[0].purchase_pizza(user_budget)
else:
    print("Sorry, your budget is too low to buy any pizza.")

 



       
