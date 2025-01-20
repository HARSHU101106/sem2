n = int(input("Enter the range (n): "))
arr = list(map(int, input("Enter the array elements: ").split()))
expected_sum = n * (n + 1) // 2
actual_sum = sum(arr)
print("Missing number is:", expected_sum - actual_sum)
