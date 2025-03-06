with open("1.txt","w") as f:
    f.write("FILE HANDLING\n")
print("FILE WRITTEN SUCCESSFULLY!")
with open("1.txt","r") as f:
    filecontent=f.read()
    print(filecontent)
with open("1.txt","a") as f:
    f.write("NEW LINE ADDED")
print("CONTENT ADDED SUCCESSFULLY!")
