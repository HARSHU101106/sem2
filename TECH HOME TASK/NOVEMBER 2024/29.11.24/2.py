'''2. Scenario: Food Delivery System
Create a system where:
• Restaurant handles the menu and food preparation.
• Delivery manages the delivery details and rider information.
• Order combines both Restaurant and Delivery to process food orders 
and manage delivery logistics'''
class Restaurant:
    def __init__(self):
        self.menu = {}
    def add_food_item(self, name, price, preparation_time):
        self.menu[name] = {'price': price, 'preparation_time': preparation_time}
    def display_menu(self):        
        if self.menu:
            print("Menu:")
            for name, details in self.menu.items():
                print(f"{name}: ${details['price']} (Preparation Time: {details['preparation_time']} minutes)")
        else:
            print("Menu is empty.")
    def prepare_food(self, food_item):
        if food_item in self.menu:
            print(f"Preparing {food_item}... (Time: {self.menu[food_item]['preparation_time']} minutes)")
            return self.menu[food_item]['preparation_time']
        else:
            print(f"{food_item} is not available on the menu.")
            return 0
class Delivery:
    def __init__(self):
        self.riders = {}
    def add_rider(self, rider_id, name):        
        self.riders[rider_id] = {'name': name, 'status': 'Available'}
    def assign_rider(self, rider_id, order_id):
        if rider_id in self.riders:
            self.riders[rider_id]['status'] = f"Delivering order {order_id}"
            print(f"Rider {self.riders[rider_id]['name']} is assigned to order {order_id}.")
            return rider_id
        else:
            print(f"Rider {rider_id} not found.")
            return None
    def track_delivery(self, rider_id):
        if rider_id in self.riders:
            print(f"Rider {self.riders[rider_id]['name']} status: {self.riders[rider_id]['status']}")
        else:
            print("Rider not found.")
class Order:
    def __init__(self, restaurant, delivery):
        self.restaurant = restaurant
        self.delivery = delivery
        self.orders = {}
    def create_order(self, order_id, food_items, rider_id):
        if not food_items:
            print("No food items selected.")
            return
        preparation_time = 0
        for food_item in food_items:
            preparation_time += self.restaurant.prepare_food(food_item)
        rider = self.delivery.assign_rider(rider_id, order_id)
        if rider is not None:
            print(f"Order {order_id} is being processed. Total preparation time: {preparation_time} minutes.")
            self.orders[order_id] = {'food_items': food_items, 'rider_id': rider, 'status': 'Preparing'}
            self.delivery.track_delivery(rider_id)
        else:
            print("Delivery assignment failed.")
    def complete_order(self, order_id):
        if order_id in self.orders:
            self.orders[order_id]['status'] = 'Delivered'
            rider_id = self.orders[order_id]['rider_id']
            self.delivery.riders[rider_id]['status'] = 'Available'
            print(f"Order {order_id} has been delivered.")
            self.delivery.track_delivery(rider_id)
        else:
            print(f"Order {order_id} not found.")
restaurant = Restaurant()
restaurant.add_food_item("Pizza", 12.99, 15)
restaurant.add_food_item("Burger", 8.99, 10)
restaurant.add_food_item("Pasta", 10.49, 12)
delivery = Delivery()
delivery.add_rider(1, "John")
delivery.add_rider(2, "Alice")
order_system = Order(restaurant, delivery)
restaurant.display_menu()
order_system.create_order(101, ["Pizza", "Pasta"], 1)
delivery.track_delivery(1)
order_system.complete_order(101)
delivery.track_delivery(1)
