n = int(input())
a = [int(x) for x in input().split()]

dp = [False] * (10**6 + 1)
dp[0] = True
m = 0
for x in a:
    for s in range(m, -1, -1):
        dp[s + x] = dp[s + x] or dp[s]
    m += x

r = []
for i in range(1, m + 1):
    if dp[i]: r.append(i)
print(len(r))
print(*r)
