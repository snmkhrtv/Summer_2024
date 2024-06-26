matrix = [
    [2, 3, 1, 0, 5],
    [1, 5, 1, 0, 1],
    [4, 2, 1, 0, 4],
    [1, 5, 1, 0, 1],
    [4, 2, 1, 0, 1]
]

def min_path(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    dp[0][0] = matrix[0][0]
    for i in range(1, rows):
        dp[i][0] = dp[i-1][0] + matrix[i][0]
    for j in range(1, cols):
        dp[0][j] = dp[0][j-1] + matrix[0][j]

    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = matrix[i][j] + min(dp[i-1][j], dp[i][j-1])

    return dp[rows-1][cols-1]

print(min_path(matrix))
