def is_disarium(num):
    digits = str(num)
    length = len(digits)
    disarium_sum = sum(int(digits[i]) ** (i + 1) for i in range(length))
    return disarium_sum == num
num = int(input("Enter a number: "))
if is_disarium(num):
    print(f"{num} is a Disarium number.")
else:
    print(f"{num} is not a Disarium number.")
