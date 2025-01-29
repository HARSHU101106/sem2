'''1. Create a class that validates the password which contains various methods to validate the 
password.
Get input from the user and validate the password.
Write a program to validate the password based on these rules and provide feedback(Valid 
or invalid).
Password rules:
At least one uppercase letter.
At least one lowercase letter.
At least one digit.
At least one special character.
Minimum length of 8 characters'''
class password:
    def validate(text):
        uppercase_count=0
        lowercase_count=0
        digit_count=0
        special_count=0
        length=len(text)
        for i in text:
            if i.isupper():
                uppercase_count+=1
            elif i.islower():
                lowercase_count+=1
            elif i.isdigit():
                digit_count+=1 
            else:
                special_count+=1 
        if uppercase_count>=1 and lowercase_count>=1 and digit_count>=1 and special_count>=1 and length>=8:
            if text[0].isupper():
                print("your password is valid")
            else:
                print("your password is not valid")
        else:
                print("your password is not valid")
user_input=input()
password.validate(user_input)