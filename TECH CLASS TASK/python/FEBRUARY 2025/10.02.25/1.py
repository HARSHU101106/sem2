rows=int(input())
cols=int(input())
for i in range(1,rows+1):
    for j in range(1,cols+1):
        if i==1 or i==4 or i==7 or j==cols:
            print("+",end=" ")
        else:
            print(" ",end=" ")
    print()
