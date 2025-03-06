rows=6
cols=5
for i in range(1,rows+1):
    for j in range(1,cols+1):
        if i==rows or j==3 or (i==2 and j==2) or (i==3 and j==2):
            print("+",end=" ")
        else:
            print(" ",end=" ")
    print()