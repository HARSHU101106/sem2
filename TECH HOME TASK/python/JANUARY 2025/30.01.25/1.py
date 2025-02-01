import re

class UserInput:
    def __init__(self):
        self.name = ""
        self.password = ""
        self.email = ""
        self.n = 0

    def validate_name(self, name):
        return bool(re.match(r'^(?=.*[0-9])(?=.*[^a-zA-Z0-9])([a-zA-Z0-9][^ ]*)$', name))

    def validate_password(self, password):
        return bool(re.match(r'^[a-zA-Z#_@]{1,8}$', password))

    def validate_email(self, email):
        return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))

    def get_valid_input(self):
        while True:
            self.name = input("Enter your Name: ")
            if self.validate_name(self.name):
                break
            print("Invalid Name! It must contain exactly one number and one special character.")

        while True:
            self.password = input("Enter your Password: ")
            if self.validate_password(self.password):
                break
            print("Invalid Password! It must not contain numbers or special characters except (#, _, @) and must be at most 8 characters long.")

        while True:
            self.email = input("Enter your Email Address: ")
            if self.validate_email(self.email):
                break
            print("Invalid Email Address! Please enter a valid format (e.g., example@mail.com).")

        while True:
            try:
                self.n = int(input("How many times do you want to Print? "))
                if self.n > 0:
                    break
                print("Number must be greater than zero.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")

    def display_output(self):
        print(f"{self.name} Wants to Print {self.n} Times and send Mail to {self.email}.")
        print(f"Your password {self.password} will be encrypted and will be stored.")

if __name__ == "__main__":
    user = UserInput()
    user.get_valid_input()
    user.display_output()
