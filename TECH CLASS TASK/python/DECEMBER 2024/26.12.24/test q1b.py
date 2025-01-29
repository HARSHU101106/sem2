def pangram(strings):
    lower=False
    for i in strings:
        if i.islower():
            lower=True
        else:
            lower=False
            break
    strings1=[]
    strings2=[]
    strings3=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if lower==True:
        for i in strings:
            if i in strings3 and i not in strings1:
                strings1.append(i)
            elif i in strings3 and i in strings1:
                strings2.append(i)
    count=0
    for i in strings1:
        count+=1
    if count==26:
        return "Pangram"
    else:
        return "Not a pangram"
n=input()
print(pangram(n))

