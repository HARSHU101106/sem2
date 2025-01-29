num = list(map(int, input("ENTER THE ELEMENTS OF THE ARRAY SEPARATED BY SPACES: ").split()))
even = []
odd = []
for idx, value in enumerate(num):
    if idx % 2 == 0:
        even.append((idx, value))  
    else:
        odd.append((idx, value))   
print("ELEMENTS AT ODD POSITION:")
for idx, value in odd:
    print(f"INDEX: {idx}, VALUE: {value}")
print("ELEMENTS AT EVEN POSITION:")
for idx, value in even:
    print(f"INDEX: {idx}, VALUE: {value}")

