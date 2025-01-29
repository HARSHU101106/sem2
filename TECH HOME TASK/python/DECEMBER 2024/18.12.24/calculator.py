class Calculator:
    def calculate(self, *args):
        if not all(isinstance(arg, (int, float)) for arg in args):
            raise ValueError("All arguments must be integers or floats.")
        if len(args) == 1:
            return args[0] ** 2
        elif len(args) == 2:
            return args[0] + args[1]
        elif len(args) == 3:
            return args[0] * args[1] * args[2]
        else:
            raise ValueError("Invalid number of arguments. Provide 1, 2, or 3 arguments.")
try:
    calc = Calculator()
    print(calc.calculate(5))         
    print(calc.calculate(5, 3))       
    print(calc.calculate(2, 3, 4))    
    print(calc.calculate(5, "a"))    
except ValueError as e:
    print(e)
