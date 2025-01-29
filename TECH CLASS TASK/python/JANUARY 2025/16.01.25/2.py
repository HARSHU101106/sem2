arr = list(map(int, input("Enter the array elements: ").split()))
seen = set()
duplicates = set()
for num in arr:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)
print("Duplicates are:", list(duplicates))
