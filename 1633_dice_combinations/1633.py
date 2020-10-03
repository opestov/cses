n = int(input())
p = 10**9 + 7

dp = [0] * (n + 10)
dp[0] = 1
for i in range(1, 7):
    dp[i] = 1 << (i - 1)

for i in range(7, n + 1):
    dp[i] = dp[i - 1] * 2 - dp[i - 7]
    if dp[i] >= p: dp[i] -= p
    if dp[i] < 0: dp[i] += p
print(dp[n])
