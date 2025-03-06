def print_pattern(N):
    for i in range(N):
        first_char = chr(ord('a') + i)  
        second_char = chr(ord('a') + i + 1)  
        pattern = (first_char + second_char) * 2  
        print(pattern)
N = int(input("Enter a number: "))
print_pattern(N)
