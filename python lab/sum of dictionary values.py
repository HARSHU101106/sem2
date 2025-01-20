n = int(input("Enter the number of items in the dictionary: "))
my_dict = {}
for _ in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    my_dict[key] = value
total_sum = sum(my_dict.values())
print("Sum of all items in the dictionary:", total_sum)
