def details():
    name=input("ENTER YOUR NAME:")
    department=input("ENTER YOUR DEPARTMENT:")
    password=input("ENTER YOUR PASSWORD:")
    retype=input("RETYPE YOUR PASSWORD")
    if name.isalpha():
        print("YOUR ENCODED NAME IS:",end=" ")
        for i in range(len(name)):
             print("X",end="")
        print("-Fresher")
    else:
        raise ValueError ("NAME SHOULD NOT CONTAIN ANY NUMBERS OR SPEACIAL CHARACTERS")
    print("YOUR DEPARTMENT IS",end=" ")
    for i in range(len(department)):
         print("X",end="")
    print()
    special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"
    digit = any(char.isdigit() for char in password)
    special = any(char in special_characters for char in password)
    if len(password) < 8 or digit or special:
        print("YOUR PASSWORD IS:",end=" ")
        for i in range(len(password)):
             print("X",end="")
    else:
        raise ValueError ("PASSWORD SHOULD CONTAIN ATLEAST ONE NUMBER AND ONE SPEACIAL CHARACTER AND LENGHT MUST BE LESS THAN 8")
    while password!=retype:
        retype=input("RETYPE YOUR PASSWORD")
    
        
try:
    details()    
except ValueError as e:
        print(e)
