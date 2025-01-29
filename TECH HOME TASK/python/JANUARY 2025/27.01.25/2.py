num=int(input("ENTER THE TOTAL NUMBER OF ELEMENTS IN LIST:"))
lst=[]
for i in range(num):
    lst.append(int(input(F"ENTER THE ELEMENT SHOULD BE IN LIST:")))
n=int(input("ENTER THE ELEMENT WHOSE FIRST OCCURENCE TO BE REMOVED:"))
for i in lst:
    if i is n:
        lst.remove(i)
        break
print("NEW LIST:",lst)