n, s = map(int, input().split())
c = [int(x) for x in input().split()]
p = [int(x) for x in input().split()]

dp = [0] * (s + 1)
for i in range(n):
    pages, price = p[i], c[i]
    for j in range(s, price - 1, -1):
        dp[j] = max(dp[j], dp[j - price] + pages)
print(max(dp))
