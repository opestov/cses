n, m = map(int, input().split())
n, m = max(n, m), min(n, m)
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    r = dp[i]
    for j in range(1, i):
        c = dp[j]
        z = i * j
        for k in range(1, (i + 2) // 2):
            z = min(z, c[k] + c[i - k] + 1)
        for k in range(1, (j + 2) // 2):
            z = min(z, r[k] + r[j - k] + 1)
        dp[i][j] = dp[j][i] = z

print(dp[n][m])
