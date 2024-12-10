'''1. Multiple inheritance example - Imagine a Smartphone that combines features of a Camera and a 
Phone. Use multiple inheritance to implement the following.
The Camera class - variable resolution and method (Take photo)
The Phone class –Phone number as variable with methods such as making calls and sending 
messages.
The Smartphone class inherits from both, combining the features of both a camera and a phone
with additional variables such as brand and model. Method in smart phone is : display device 
information.
'''
class Camera:
    def __init__(self, resolution):
        self.resolution = resolution
    def take_photo(self):
        print(f"Photo taken at {self.resolution} resolution.")
class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
    def make_call(self, number):
        print(f"Calling {number} from {self.phone_number}...")
    def send_message(self, number, message):
        print(f"Sending message to {number} from {self.phone_number}: {message}")
class Smartphone(Camera, Phone):
    def __init__(self, resolution, phone_number, brand, model):
        Camera.__init__(self, resolution)
        Phone.__init__(self, phone_number)
        self.brand = brand
        self.model = model
    def display_device_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Resolution: {self.resolution}")
        print(f"Phone Number: {self.phone_number}")
smartphone = Smartphone("12MP", "7604830551", "VIVO", "Y27")
smartphone.display_device_info()
smartphone.take_photo()
smartphone.make_call("9884088249")
smartphone.send_message("9884088249", "HELLO DEAR, HOW ARE YOU?")
