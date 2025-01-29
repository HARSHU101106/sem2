n=int(input())
L=[]
for i in range(n):
    L.append(int(input()))
oddcount=0
evencount=0
for j in L:
    if j%2==0:
        evencount+=1
    else:
        oddcount+=1
print(f"the number of even elements in the array: {evencount}")
print(f"the number of odd elements in the array: {oddcount}")

