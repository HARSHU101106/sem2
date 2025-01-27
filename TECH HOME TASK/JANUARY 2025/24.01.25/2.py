p = int(input("Enter the first value: ")) 
q = int(input("Enter the second value: ")) 
r = int(input("Enter the third value: ")) 
add = p +q
sub= p - q
mul=p * q
div= p/q 
print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {mul}")
print(f"Division: {div}")
print("\nBefore Swapping:")
print(f"First value: {p}")
print(f"Second value: {q}")
print(f"Third value: {r}")
p = r
q=p
r=q
print("\nAfter Swapping:")
print(f"First value: {p}")
print(f"Second value: {q}")
print(f"Third value: {r}")
