def solution(triangle):
    dp = [[0, *t, 0] for t in triangle]
    for i in range(1, len(triangle)):
        for j in range(1, i + 2):
            dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])

    return max(dp[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))