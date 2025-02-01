n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    num = i
    diff = n - 1
    for j in range(i):
        print(num, end=" ")
        num += diff
        diff -= 1
    print()