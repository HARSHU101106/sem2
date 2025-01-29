print("task1:area of square")
print("task2:area of rectangle")
print("task3:area of triangle")
print("task4:area of circle")
choice = int(input(" Enter task (1,2,3,4) to be perfomed:"))
if choice == 1:
    a=float(input("Enter the side length of a square:"))
    print("The area of a square is:",a**2,"square units")
elif choice == 2:
    l=float(input("Enter the length of a rectangle in:"))
    b=float(input("Enter the breadth of a rectangle in:"))
    print("The area of rectangle is:",l*b,"square units")
elif choice == 3:
    h=float(input("Enter the height of a triangle:"))
    base=float(input("Enter the base of a triangle:"))
    print("the area of triangle is:",(1/2)*base*height,"square units")
elif choice == 4:
    r= float(input("Enter the radius of a circle:"))
    print("the area of a circle is:",3.14*(r**2),"square units")