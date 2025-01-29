class Factorial:
    def calculate(self, n):
        if n == 0 or n == 1:
            return 1
        return n * self.calculate(n - 1)
def sum_of_factorials(n):
    factorials = []
    total_sum = 0
    fact_calculator = Factorial()
    for i in range(1, n + 1):
        fact = fact_calculator.calculate(i)
        factorials.append(f"{i}! = {fact}")
        total_sum += fact
    return total_sum
n = int(input())
if n > 0:
    total_sum = sum_of_factorials(n)
    print(f"Sum of all factorials: {total_sum}")
