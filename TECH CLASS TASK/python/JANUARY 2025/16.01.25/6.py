arr = list(map(int, input("Enter the array elements: ").split()))
target = int(input("Enter the target sum: "))
pairs = []
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            pairs.append((arr[i], arr[j]))
print("Pairs that sum to", target, "are:", pairs)
