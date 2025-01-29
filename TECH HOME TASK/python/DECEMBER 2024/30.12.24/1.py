class StringAnalyzer:
    def __init__(self, input_string):
        self.input_string = input_string
    def analyze(self):
        alphabets = sum(char.isalpha() for char in self.input_string)
        digits = sum(char.isdigit() for char in self.input_string)
        specials = len(self.input_string) - alphabets - digits
        return alphabets, digits, specials
input_string = input("Enter a string: ")
analyzer = StringAnalyzer(input_string)
alphabets, digits, specials = analyzer.analyze()
print("Alphabetic Characters:", alphabets)
print("Numeric Characters:", digits)
print("Special Characters:", specials)
