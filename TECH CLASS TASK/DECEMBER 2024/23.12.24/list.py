n=int(input("Enter the number of elements in the list:"))
list1=[]
for i in range(n):
    list1.append(int(input(f"enter the element")))
list2=[]
dup=[]
for i in list1:
    if i not in list2:
        list2.append(i)
    elif i in list2:
        dup.append(i)
print("the list after removing duplicates is:",list2)
list2.sort(reverse=True)
print("the list that is sorted in descending order is:",list2)
#4min 49sec
