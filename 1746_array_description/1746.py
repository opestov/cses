n, m = map(int, input().split())
a = [int(x) - 1 for x in input().split()]
B = 10**9 + 7

dp = [[0] * (m + 1), [0] * (m + 1)]
p = 1

if a[0] == -1:
    for j in range(m):
        dp[0][j] = 1
else:
    dp[0][a[0]] = 1

for i in range(1, n):
    zz, m1 = dp[p], dp[1 - p]
    if a[i] == -1:
        for j in range(m):
            zz[j] = (m1[j - 1] + m1[j] + m1[j + 1]) % B
    else:
        for j in range(m):
            zz[j] = 0
        zz[a[i]] = (m1[a[i] - 1] + m1[a[i]] + m1[a[i] + 1]) % B
    p = 1 - p

print(sum(dp[1 - p]) % B)
