class inventory:
    def getprodet(self):
        self.proId=int(input("Enter the product Id: "))
        self.proname=input("Enter the product Name: ")
        self.procount=int(input("Enter the product count: "))
class invent(inventory):
    def getprodet(self):
        return super().getprodet()
    def dispprodet(self):
        print(f"PRODUCT ID = {self.proId} \n PRODUCT NAME = {self.proname} \n PRODUCT COUNT = {self.procount}")
g=invent()
g.dispprodet()