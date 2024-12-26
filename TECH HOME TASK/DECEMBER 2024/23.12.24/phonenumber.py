import re
text = input("Enter the text: ")
pattern = r'\b\d{10}\b|\b(?:\d{3}-\d{3}-\d{4})\b|\b(?:\(\d{3}\) \d{3}-\d{4})\b'
phone_numbers = re.findall(pattern, text)
if phone_numbers:
    print("Extracted phone numbers:", phone_numbers)
else:
    print("No phone numbers found.")
