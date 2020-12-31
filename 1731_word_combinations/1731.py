import sys

M = 10**9 + 7
s = [ord(x) - ord('a') for x in sys.stdin.readline().strip()]
n = int(sys.stdin.readline())
words = sys.stdin.read().split()

t, p, c, e = [[1] * 26, [0] * 26], [0, 0], [0, 0], [0, 0]
o = [[] for _ in range(len(s))]
for w in words:
    if len(w) > len(s): continue

    v = 1
    for i in range(len(w)):
        j = ord(w[i]) - ord('a')
        if t[v][j] == 0:
            c.append(j), p.append(v), t.append([0] * 26), e.append(0)
            o[i].append(len(p) - 1)
            t[v][j] = len(p) - 1
        v = t[v][j]
    e[v] = len(w)

f, link = [0] * len(p), [0] * len(p)
for i in range(len(s)):
    for v in o[i]:
        u, x = f[p[v]], c[v]
        while t[u][x] == 0:
            u = f[u]
        w = t[u][x]
        f[v] = w
        link[v] = w if e[w] else link[w]

dp = [0] * (len(s) + 1)
dp[0] = 1

v = 1
for i in range(len(s)):
    x = s[i]
    while t[v][x] == 0:
        v = f[v]
    v = t[v][x]

    u = v if e[v] else link[v]
    while u:
        dp[i + 1] += dp[i + 1 - e[u]]
        if dp[i + 1] >= M:
            dp[i + 1] -= M
        u = link[u]

sys.stdout.write(str(dp[len(s)]))
