class Vehicle:
    def fuelType(self):
        return "General Fuel"

class Car(Vehicle):
    def fuelType(self):
        return "Petrol or Diesel"

class Bike(Vehicle):
    def fuelType(self):
        return "Petrol"

# Creating objects of Car and Bike
car = Car()
bike = Bike()

# Demonstrating method overriding
print("Car fuel type:", car.fuelType())
print("Bike fuel type:", bike.fuelType())
