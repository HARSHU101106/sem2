add=lambda a,b:a+b
print(add(3,4))

l1=list(map(int,input().split()))
square=list(map(lambda X:X**2,l1))
print(square)

l2=list(map(int,input().split()))
even=filter(lambda X:X%2==0,1,2)
print(list(even))

t=[(1,2),(3,3),(2,1)]
t1=sorted(t,key=lambda X:X[0] )
print(t1)

mul=lambda a,b:a*b
print(mul(2,4))

l3=list(map(int,input().split()))
cube=list(map(lambda X: X**3,l3))
for i in cube:
    print(i,end=" ")



