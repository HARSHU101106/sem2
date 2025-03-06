n=int(input())
lst=[]
for i in range(n):
    lst.append(input())
if not lst:
    print("")
else:
    prefix = lst[0]
    for s in lst[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                print("")
                break
    else:
        print(prefix)

