'''Q-1) Vehicle – example hybrid inheritance
1. Vehicle (Base Class): Represents a general vehicle with basic attributes like 
make, model, and year.
2. Car (Derived from Vehicle): Represents cars, which have additional 
features like the number of doors and trunk capacity.
3. Truck (Derived from Vehicle): Represents trucks, which have attributes 
like cargo capacity and number of axles.
4. PickupTruck (Derived from both Car and Truck): A specific type of vehicle 
that combines features of both cars (passenger-friendly) and trucks (cargo-friendly). Method – display all the features.'''
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display_vehicle_info(self):
        return f"Make: {self.make},\n Model: {self.model}, \nYear: {self.year}"
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors, trunk_capacity):
        Vehicle.__init__(self, make, model, year)
        self.num_doors = num_doors
        self.trunk_capacity = trunk_capacity
    def display_car_info(self):
        return f"{self.display_vehicle_info()},\n Number of Doors: {self.num_doors}, \nTrunk Capacity: {self.trunk_capacity} liters"
class Truck(Vehicle):
    def __init__(self, make, model, year, cargo_capacity, num_axles):
        super().__init__(make, model, year)
        self.cargo_capacity = cargo_capacity
        self.num_axles = num_axles
    def display_truck_info(self):
        return f"{self.display_vehicle_info()},\n Cargo Capacity: {self.cargo_capacity} tons,\n Number of Axles: {self.num_axles}"
class PickupTruck(Car, Truck):
    def __init__(self, make, model, year, num_doors, trunk_capacity, cargo_capacity, num_axles):
        Car.__init__(self, make, model, year, num_doors, trunk_capacity)
        Truck.__init__(self, make, model, year, cargo_capacity, num_axles)
    def display_all_features(self):
        return (
            f"{self.display_vehicle_info()},\n Number of Doors: {self.num_doors}, "f"\nTrunk Capacity: {self.trunk_capacity} liters,\nCargo Capacity: {self.cargo_capacity} tons, "f"\nNumber of Axles: {self.num_axles}")
pickup = PickupTruck("Toyota", "Hilux", 2023, 4, 500, 1.5, 2)
print(pickup.display_all_features())
