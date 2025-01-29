word1 = input("Enter first string: ")
word2 = input("Enter second string: ")
merged_string = ""
i, j = 0, 0
while i < len(word1) or j < len(word2):
    if i < len(word1):
        merged_string += word1[i]
        i += 1
    if j < len(word2):
        merged_string += word2[j]
        j += 1
print("Merged string:", merged_string)
