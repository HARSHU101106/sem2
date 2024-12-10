'''2. Scenario: Cosmetic Product Information
• Create a class named Cosmetics
• Track a cosmetic product's name, brand, price, and category.
• Use a default constructor to initialize these attributes with default values.
• Display all the information. (Action –method)'''
class Cosmetics:
    def __init__(self,name="hair care kit",brand="kosmoderma",price=5000,category="haircare"):
        self.name = name
        self.brand =brand
        self.price =price
        self.category =category
    def display_info(self):
        print("Cosmetic Product Information:")
        print(f"Name: {self.name}")
        print(f"Brand: {self.brand}")
        print(f"Price: ${self.price:.2f}")
        print(f"Category: {self.category}")
default_product = Cosmetics()
default_product.display_info()
2..