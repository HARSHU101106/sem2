class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement this method")

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")

class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")

class UPI(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using UPI.")

amount = float(input("Enter the amount to pay: "))

payments = [CreditCard(), PayPal(), UPI()]

for payment in payments:
    payment.pay(amount)
