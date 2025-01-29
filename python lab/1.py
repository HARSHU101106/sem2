print("Enter 'c' to convert from Celsius to Farenheit")
print("Enter 'f' to convert from Farenheit to Celsius")
choice=input("Enter your choice:")
if choice == 'c':
    celsius=float(input("Enter temperature in Celsius:"))
    farenhite=(celsius* 9/5)+32
    print('%.2f Celsius is: %0.2f Farenheit' %(celsius,farenhite))
elif choice == 'f':
    farenhite = float(input("Enter temperature in Farenheit:"))
    celsius = (farenhite - 32) * 5/9
    print('%.2f Farenheit is: %0.2f Celsius' %(farenhite,celsius))
else:
    print("Invalid Input")