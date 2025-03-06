num_of_elements = int(input("Enter the number of elements in the list: "))
lst1 = []
for i in range(num_of_elements):
    lst1.append(int(input(f"Enter element {i+1}: ")))
kth_large = int(input("Enter which largest element should be printed: "))
lst1.sort(reverse=True)
if 1 <= kth_large <= len(lst1):
    print(f"The {kth_large}th largest element is: {lst1[kth_large - 1]}")
else:
    print("Invalid input for kth largest element.")
