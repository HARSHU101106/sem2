import re
email = input("Enter an email address: ")
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
if re.match(pattern, email):
    print("Valid email address.")
else:
    print("Invalid email address.")
