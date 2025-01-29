def sum_2d_array(matrix):
    total = 0
    for row in matrix:
        total += sum(row)
    return total
rows = int(input("Enter the number of rows: "))
matrix = []
for i in range(rows):
    row = list(map(int, input(f"Enter row {i + 1} (space-separated): ").split()))
    matrix.append(row)
print("Sum of all elements:", sum_2d_array(matrix))
