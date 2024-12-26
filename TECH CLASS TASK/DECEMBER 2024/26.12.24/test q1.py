import re
def validate(num):
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    if re.match(pattern, num) is not None:
        return "Valid"
    else:
        raise ValueError("Invalid")
phnnum = input("Enter a phone number:")
try:
    print(validate(phnnum))
except ValueError as e:
    print(e)
