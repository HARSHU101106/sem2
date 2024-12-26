class Product:
    def __init__(self, base_price, discount_percentage=0, tax_percentage=0):
        self.base_price = base_price
        self.discount_percentage = discount_percentage
        self.tax_percentage = tax_percentage
    def calculate_final_price(self):
        if self.base_price < 0:
            raise ValueError("Base price cannot be negative.")
        if self.discount_percentage < 0:
            raise ValueError("Discount percentage cannot be negative.")
        if self.tax_percentage < 0:
            raise ValueError("Tax percentage cannot be negative.")
        discount_amount = (self.discount_percentage / 100) * self.base_price
        price_after_discount = self.base_price - discount_amount
        tax_amount = (self.tax_percentage / 100) * price_after_discount
        final_price = price_after_discount + tax_amount
        return round(final_price, 2)
try:
    product = Product(base_price=100, discount_percentage=10, tax_percentage=5)
    final_price = product.calculate_final_price()
    print(f"The final price of the product is: ${final_price}")
except ValueError as e:
    print(e)
