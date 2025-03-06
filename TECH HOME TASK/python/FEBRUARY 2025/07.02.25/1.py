n=int(input())
fact=1
for i in range(1,n+1):
    fact*=i
count=0
for i in str(fact):
    if i == "0":
        count+=1
print(count)