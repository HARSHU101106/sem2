arr = [3, 3, 4, 2, 3, 3, 3, 2, 3]
n = len(arr)

for num in set(arr):
    if arr.count(num) > n // 2:
        print(num)
        break