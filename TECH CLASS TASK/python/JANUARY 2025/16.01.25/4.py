from collections import Counter
arr = list(map(int, input("Enter the array elements: ").split()))
n = len(arr)
counts = Counter(arr)
majority_element = None
for key, count in counts.items():
    if count > n // 2:
        majority_element = key
        break
print("Majority element is:", majority_element if majority_element else "No majority element")
