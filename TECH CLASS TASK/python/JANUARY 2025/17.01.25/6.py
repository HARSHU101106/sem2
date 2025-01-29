def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
rows = int(input("Enter the number of rows: "))
matrix = []
for i in range(rows):
    row = list(map(int, input(f"Enter row {i + 1} (space-separated): ").split()))
    matrix.append(row)
print("Transposed matrix:")
transposed = transpose(matrix)
for row in transposed:
    print(row)
