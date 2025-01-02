class Creditcardpayment:
    def pay(self,amount):
        return f"paid {amount} using creditcard"
class Paypalpayment:
    def pay(self,amount):
        return f"paid {amount} using paypal"
class Debitcardpayment:
    def pay(self,amount):
        return f"paid {amount} using debitcard"
def process_payment(payment_method,amount):
    print(payment_method.pay(amount))
cc=Creditcardpayment()
process_payment(cc,200)
pp=Paypalpayment()
process_payment(pp,220)
dd=Debitcardpayment()
process_payment(dd,222)
 
