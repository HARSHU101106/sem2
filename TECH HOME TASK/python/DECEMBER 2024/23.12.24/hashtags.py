import re
text = input("Enter the text: ")
pattern = r'#\w+'
hashtags = re.findall(pattern, text)
if hashtags:
    print("Extracted hashtags:", hashtags)
else:
    print("No hashtags found.")
