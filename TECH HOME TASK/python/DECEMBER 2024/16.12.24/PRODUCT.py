#2. 
class Product:
    def _init_(self, name, price, stock):
        self._name = name
        self.set_price(price)
        self.set_stock(stock)

    def set_price(self, price):
        if price <= 0:
            raise ValueError("Price must be greater than 0.")
        self._price = price

    def set_stock(self, stock):
        if not isinstance(stock, int) or stock < 0:
            raise ValueError("Stock must be a non-negative integer.")
        self._stock = stock

    def get_stock(self):
        return self._stock

product = Product("Laptop", 1500, 10)
product.set_price(2000)
product.set_stock(20)
print(product.get_stock())