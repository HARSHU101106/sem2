n=int(input("ENTER THE TOTAL NUMBER OF ELEMENTS:"))
lst=[]
for i in range(n):
    lst.append(input("ENETR THE ELEMENT OF THE ARRAY"))
print("YOUR INVERSE ORDER ARRAY IS:",lst[::-1])
print("YOUR NON-INVERSE ORDER ARRAY IS:",lst)