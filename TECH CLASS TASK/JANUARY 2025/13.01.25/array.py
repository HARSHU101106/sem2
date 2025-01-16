n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
index = 0#1#2
for i in range(n):
    if l[i] != 0:
        l[index] = l[i]
        index += 1
for i in range(index, n):
    l[i] = 0
print(l)
index = n - 1
for i in range(n - 1, -1, -1):
    if l[i] != 0:
        l[index] = l[i]
        index -= 1
for i in range(index + 1):
    l[i] = 0
print(l)
