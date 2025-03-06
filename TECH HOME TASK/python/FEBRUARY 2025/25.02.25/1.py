def spiral_pattern(n, m):
    matrix = [[0] * m for _ in range(n)]
    top, left = 0, 0
    bottom, right = n - 1, m - 1
    num = 1
    while num <= n * m:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1
    for row in matrix:
        print("  ".join(f"{num:2}" for num in row))
spiral_pattern(5, 5)
