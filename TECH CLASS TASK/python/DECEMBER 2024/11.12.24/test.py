def take_inp():
    name=input("Enter First Name:")
    b=[]
    for i in name:
       b.append(i)
    for i in b:
        if i in ['0','1','2','3','4','5','6','7','8','9']:
            b.remove(i)
    print("Hi! Your Entered Input Is")
    for i in b:
        print(i,end=" ")
a=take_inp()
'''
def chara():
    name=input("Enter Name:")
    special=[]
    character=[]
    number=[]
    for i in name:
        if type(i) is chr:
            character.append(i)
        elif type(i) is int:
            number.append(i)
        else:
            special.append(i)
    print("Your Entered Characters are-",end=" ")
    for i in character:
        print(i,end=" ")
    print("Your Entered Special Characters are-",end=" ")
    for i in special:
        print(i,end=" ")  

a=chara()'''
def chara():
     name=input("\nEnter Name:")
     character=[]
     special=[]
     for i in name:
          if i in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
               character.append(i)
          elif i not in ['0','1','2','3','4','5','6','7','8','9']:
               special.append(i)
     print("Your Entered Characters are-",end=" ")
     for i in character:
           print(i,end=" ")
     print("Your Entered Special Characters are-",end=" ")
     for i in special:
           print(i,end=" ")  
a=chara()