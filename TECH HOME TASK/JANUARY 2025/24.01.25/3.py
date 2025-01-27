username=input("Enter first name:") 
filtered_name="" 
for char in username:
 if not char.isdigit():
   filtered_name+=char 
print("Hi!!! Your entered input is:",filtered_name) 
print() 
username=input("Enter first name:") 
characters="" 
spl_chars="" 
for char in username:
 if char.isalpha():
   characters+=char
 elif not char.isdigit():
   spl_chars+=char 
print("Your entered characters are:",characters) 
print("Your entered special characters are:",spl_chars)