def reverse_string(s):
    if len(s) == 0:
        return s
    return s[-1] + reverse_string(s[:-1])
string = input("Enter a string to reverse: ")
print("Reversed string:", reverse_string(string))
