first_name=input("Enter the first name:") 
last_name=input("Enterr the last name:") 
fullname=first_name+last_name 
print("Your name is:",fullname) 
clg=input("Enter the college name:") 
dept=input("Enter the department name:") 
print("Your college name is :",clg+" "+dept)
phone_no=input("Enter the mobile number:") 
ascii_name=[] 
for i in name:
 if i!="":
   ascii_name.append(ord(i)) 
   print(f"Your ASCII name is :{i}-{ord(i)}") 
ascii_mobile=[] 
for i in phone_no:
  if i!="":
    ascii_no=ord(i)
    ascii_mobile.append(ascii_no) 
    print(f"Your ascii mobile number is:{i}-{ascii_no}") 
for i in range(len(ascii_name)):
 for j in range(len(ascii_mobile)):
   if i==j:
     print(ascii_name[i]+ascii_mobile[j])