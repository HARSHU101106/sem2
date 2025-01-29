arr = list(map(int, input("Enter the array elements: ").split()))
is_sorted = True
for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        is_sorted = False
        break
print("Is the array sorted?:", is_sorted)
