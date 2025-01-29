num1=int(input("enter the number of elements to be appended in list 1"))
num2=int(input("enter the number of elements to be appended in list 2"))
lst1=[]
lst2=[]
for i in range(num1):
    lst1.append(int(input("enter the element to be appenden in list1")))
for j in range(num2):
    lst2.append(int(input("enter the element to be appenden in list1")))
common=[]
for i in lst1:
    if i in lst2:
        common.append(i)
print(f"the common elements in the two lists are {common}")
#2min 3sec