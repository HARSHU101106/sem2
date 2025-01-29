print("TASK1: AREA OF RECTANGLE")
print("TASK2: AREA OF SQUARE")
print("TASK3: AREA OF CIRCLE")
print("TASK4: AREA OF TRIANGLE")
choice=int(input("ENTER YOUR CHOICE (1,2,3,4):"))
if choice==1:
    length=float(input("ENTER THE LENGTH OF RECTANGLE:"))
    breadth=float(input("ENTER THE BREADTH OF RECTANGLE:"))
    arrec=length*breadth
    print(f"THE AREA OF RECTANGLE IS {arrec}")
elif choice==2:
    side=float(input("ENTER THE SIDE OF SQUARE:"))
    arsqr=side**2
    print(f"THE AREA OF SQUARE IS {arsqr}")
elif choice==3:
    radius=float(input("ENTER THE RADIUS OF THE CIRCLE:"))
    arcir=3.14*(radius**2)
    print(f"THE AREA OF CIRCLE IS {arcir}")
elif choice==4:
    height=float(input("ENTER THE HEIGHT OF TRIANGLE:"))
    base=float(input("ENTER THE BASE OF TRIANGLE:"))
    artri=(1/2)*base*height
    print(f"THE AREA OF TRIANGLE IS {artri}")
else:
    print("ENTER A VALID CHOICE")