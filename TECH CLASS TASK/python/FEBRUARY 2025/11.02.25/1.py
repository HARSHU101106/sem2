def hollow_pyramid(n):
    for i in range(1,n+1): #1|2|3|4|5
        space=" "*(n-i) # 4spaces 3spaces | 2 spaces | 1 space | 0 space
        if i==1: #first row
            print(space+"*")
        elif i==n: #last row
            print("*"*(2*n-1)) # 9 stars
        else: #middle rows
            middle_space="*"*(2*i-3) #1 space | 3 spaces |
            print(space+"*"+middle_space+"*")

n=int(input())
hollow_pyramid(n) 