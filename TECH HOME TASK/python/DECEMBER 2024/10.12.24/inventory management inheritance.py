'''Q-2) Inventory Management System [Hierarchical inheritance]
1. Product (Base Class): Defines common attributes like product ID, name, 
and price. Method to display all the info.
2. Electronics (Derived Class): Inherits from Product and adds attributes 
like warranty period and brand. Method to display all the info.
3. Clothing (Derived Class): Inherits from Product and adds attributes like 
size and material. Method to display all the info'''
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
    def display_info(self):
        print(f"Product ID: {self.product_id}, Name: {self.name}, Price: Rs.{self.price:.2f}")
class Electronics(Product):
    def __init__(self, product_id, name, price, warranty_period, brand):
        super().__init__(product_id, name, price)
        self.warranty_period = warranty_period
        self.brand = brand
    def display_info(self):
        print (f"{super().display_info()}, Warranty Period: {self.warranty_period} years, "f"Brand: {self.brand}")
class Clothing(Product):
    def __init__(self, product_id, name, price, size, material):
        super().__init__(product_id, name, price)
        self.size = size
        self.material = material
    def display_info(self):
         print(f"{super().display_info()}, Size: {self.size}, Material: {self.material}")
laptop = Electronics("E001", "Laptop", 30000.00, 2, "ASUS")
shirt = Clothing("C001", "T-Shirt", 1000.00, "L", "Cotton")
print(laptop.display_info())
print(shirt.display_info())
