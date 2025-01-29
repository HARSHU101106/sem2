sub1=float(input("ENTER THE MARK OF sub1:"))
sub2=float(input("ENTER THE MARK OF sub2:"))
sub3=float(input("ENTER THE MARK OF sub3:"))
sub4=float(input("ENTER THE MARK OF sub4:"))
sub5=float(input("ENTER THE MARK OF sub5:"))
total=sub1+sub2+sub3+sub4+sub5
per=(total/500)*100
if per>=80:
    print("GRADE A")
elif per>=70 and per<80:
    print("GRADE B")
elif per>=60 and per<70:
    print("GRADE C")
elif per>=40 and per<60:
    print("GRADE D")
elif per>=40:
    print("GRADE E")
