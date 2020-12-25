P = 10**9 + 7
n = int(input())
s = input()
m = len(s)

p = [0] * m
for i in range(1, m):
    k = p[i - 1]
    while k and s[k] != s[i]:
        k = p[k - 1]
    p[i] = k + (s[k] == s[i])

a = [[0] * 26 for _ in range(m)]
for j in range(26):
    a[0][j] = s[0] == chr(j + ord('A'))
for i in range(1, m):
    for j in range(26):
        a[i][j] = i + 1 if s[i] == chr(j + ord('A')) else a[p[i - 1]][j]

dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    di, d1 = dp[i], dp[i + 1]
    for j in range(m):
        if di[j]:
            aj = a[j]
            for k in range(26):
                t = aj[k]
                d1[t] = (d1[t] + di[j]) % P

p26 = [1] * (n + 1)
for i in range(1, n + 1):
    p26[i] = (p26[i - 1] * 26) % P

r = 0
for i in range(n + 1):
    r = (r + dp[i][m] * p26[n - i]) % P
print(r)
