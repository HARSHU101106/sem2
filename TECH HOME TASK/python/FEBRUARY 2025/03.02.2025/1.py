student={"KRISHNA":90,"GOKUL":85,"HARSHINI":100,"HARSHU":95}
ascending= dict(sorted(student.items(), key=lambda item: item[1]))
print("\n Ascending Order:",ascending)
descending= dict(sorted(student.items(), key=lambda item: item[1], reverse=True))
print("\n Descending Order:",descending)
top3= dict(sorted(student.items(), key=lambda item: item[1], reverse=True)[:3])
print("\nTOP 3:",top3)
names= dict(sorted(student.items(), key=lambda item: item[0]))
print("\nAlphabatically sorted:",names)
