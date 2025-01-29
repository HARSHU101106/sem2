class StringValidator:
    def __init__(self, input_string):
        self.input_string = input_string
    def validate(self):
        has_alphabet = any(char.isalpha() for char in self.input_string)
        has_special = any(not char.isalnum() for char in self.input_string)
        return has_alphabet and has_special
input_string = input("Enter a string: ")
validator = StringValidator(input_string)
if validator.validate():
    print("The string contains both alphabets and special characters")
else:
    print("The string does not contain both alphabets and special characters")
