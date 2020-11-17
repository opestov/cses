def read():
    global n, m, d1, h1, d2, h2
    n, m = map(int, sys.stdin.readline().split())
    a = [int(x) for x in sys.stdin.read().split()]
    d1, h1, d2, h2 = [0] * m, [0] * (n + 1), [0] * m, [0] * (n + 1)
    for i in range(0, len(a), 2):
        h1[a[i] - 1] += 1
        h2[a[i + 1] - 1] += 1
    for i in range(1, n + 1):
        h1[i] += h1[i - 1]
        h2[i] += h2[i - 1]
    for i in range(0, len(a), 2):
        u, v = a[i] - 1, a[i + 1] - 1
        d1[h1[u] - 1] = v
        h1[u] -= 1
        d2[h2[v] - 1] = u
        h2[v] -= 1


def dfs(start, d, h):
    c[start] = True
    s.append(start)
    while len(s) > 0:
        v = s.pop()
        for i in range(h[v], h[v + 1]):
            u = d[i]
            if not c[u]:
                c[u] = True
                s.append(u)


import sys

read()

c, s = [False] * n, []
x = 0
for i in range(n):
    if not c[i]:
        x = i
        dfs(i, d1, h1)

for i in range(n):
    c[i] = False
dfs(x, d2, h2)

for i in range(n):
    if not c[i]:
        print('NO', file=sys.stdout)
        print(i + 1, x + 1, file=sys.stdout)
        sys.exit(0)
print('YES', file=sys.stdout)
