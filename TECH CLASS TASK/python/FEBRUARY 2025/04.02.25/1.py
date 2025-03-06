character=input()
if 'A'<=character<='Z':
    c=ord(character)+32
    converted=chr(c)
print(converted)

string1=input()
string2=""
for i in string1:
    if 'A'<=i<='Z':
        string2+=chr(ord(i)+32)
print(string2)

string3=input()
for i in string3:
     if 'A'<=i<='Z':
         print(chr(ord(i)+32),end="")
     elif 'a'<=i<='z':
         print(chr(ord(i)-32),end="")




