string1=input().strip()
print(string1[::-1])
string2=""
length=0
for i in string1:
    length+=1
print(length)
for i in range(length-1,-1,-1):
    string2+=string1[i]
print(string2)