input_str=input()
length=len(input_str)
m=""
for i in range(length):
    if input_str[i].isdigit():
        m+=input_str[i+1]*int(input_str[i])
print(m)
