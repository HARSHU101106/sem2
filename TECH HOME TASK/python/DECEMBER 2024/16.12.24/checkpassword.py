class User:
    def __init__(self, username, password):
        self._username = username
        self._password = None
        self.set_password(password)
    def set_password(self, password):
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in password):
            raise ValueError("Password must contain at least one number.")
        if not any(char in "!@#$%^&*()-_+=<>?/|\\{}[]:;" for char in password):
            raise ValueError("Password must contain at least one special character.")
        self._password = password
    def check_password(self, input_password):
        return self._password == input_password
name=input("Enter Name")
passw=input("Ente Password")
user = User(name, passw)
print(user.check_password(passw)) 
 