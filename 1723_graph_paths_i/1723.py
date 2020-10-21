B = 10**9 + 7


def mm(a, b):
    z = len(a)
    c = [[0] * z for _ in range(z)]
    for i in range(z):
        ci, ai = c[i], a[i]
        for j in range(z):
            for k in range(z):
                ci[j] = (ci[j] + ai[k] * b[k][j]) % B
    return c


import sys

n, m, k = map(int, sys.stdin.readline().split())
e = [int(x) for x in sys.stdin.read().split()]

g = [[0] * n for _ in range(n)]
for i in range(0, len(e), 2):
    g[e[i + 1] - 1][e[i] - 1] += 1

r = [[0] * n for _ in range(n)]
for i in range(n):
    r[i][i] = 1

while k > 0:
    if k % 2 == 1:
        r = mm(r, g)
    g = mm(g, g)
    k //= 2

print(r[n - 1][0])
