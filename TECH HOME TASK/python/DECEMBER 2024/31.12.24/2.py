class Fibonacci:
    def find_first_exceeding(self, x):
        sequence = [0, 1]
        while sequence[-1] <= x:
            sequence.append(sequence[-1] + sequence[-2])
        return sequence[:-1], sequence[-1]
x = int(input())
if x >= 0:
    fib_calculator = Fibonacci()
    sequence, first_exceeding = fib_calculator.find_first_exceeding(x)
    print(f"Fibonacci sequence: {', '.join(map(str, sequence))}")
    print(f"First Fibonacci number greater than {x}: {first_exceeding}")
