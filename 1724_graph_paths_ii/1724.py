import sys

INF = 10**18 + 1
n, m, dist = map(int, sys.stdin.readline().split())
e = [int(x) for x in sys.stdin.read().split()]
aux1 = [0] * n
aux2 = [[0] * n for _ in range(n)]


def s1(d, g):
    for j in range(n):
        aux1[j] = INF
        for k in range(n):
            if d[k] < INF and g[k][j] < INF:
                aux1[j] = min(aux1[j], d[k] + g[k][j])
    for j in range(n):
        d[j] = aux1[j]


def s2(a):
    for i in range(n):
        ai, ci = a[i], aux2[i]
        for j in range(n):
            ci[j] = INF
            for k in range(n):
                if ai[k] < INF and a[k][j] < INF:
                    ci[j] = min(ci[j], ai[k] + a[k][j])
    for i in range(n):
        ai, ci = a[i], aux2[i]
        for j in range(n):
            ai[j] = ci[j]


g = [[INF] * n for _ in range(n)]
for i in range(0, len(e), 3):
    a, b, c = e[i] - 1, e[i + 1] - 1, e[i + 2]
    g[a][b] = min(g[a][b], c)

r = [INF] * n
r[0] = 0
while dist > 0:
    if dist % 2 == 1:
        s1(r, g)
    s2(g)
    dist //= 2
print(-1 if r[n - 1] == INF else r[n - 1])
