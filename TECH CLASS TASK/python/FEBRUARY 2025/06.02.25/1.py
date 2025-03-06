n=int(input())
lst=[]
for i in str(n):
    x=0
    for j in range(1,int(i)+1):
        if int(i)%j==0:
            x+=1
        else:
            continue
    if x==2:
        lst.append(int(i))
sums=0
for i in lst:
    sums+=i
print(sums)
