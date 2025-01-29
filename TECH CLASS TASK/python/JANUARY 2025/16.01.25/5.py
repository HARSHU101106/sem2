arr = list(map(int, input("Enter the array elements: ").split()))
total_sum = sum(arr)
left_sum = 0
is_balanced = False
for i in range(len(arr)):
    total_sum -= arr[i]
    if left_sum == total_sum:
        is_balanced = True
        break
    left_sum += arr[i]
print("Is the array balanced?:", is_balanced)
