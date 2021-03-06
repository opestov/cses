def read():
    global n, m, d1, h1, d2, h2
    n, m = map(int, sys.stdin.readline().split())
    a = [int(x) - 1 for x in sys.stdin.read().split()]
    d1, h1, d2, h2 = [0] * m, [0] * (n + 1), [0] * m, [0] * (n + 1)
    for i in range(0, len(a), 2):
        h1[a[i]] += 1
        h2[a[i + 1]] += 1
    for i in range(1, n + 1):
        h1[i] += h1[i - 1]
        h2[i] += h2[i - 1]
    for i in range(0, len(a), 2):
        u, v = a[i], a[i + 1]
        d1[h1[u] - 1] = v
        h1[u] -= 1
        d2[h2[v] - 1] = u
        h2[v] -= 1


def check(d, h):
    c = [False] * n
    s = [0]
    c[0] = True
    while len(s) > 0:
        v = s.pop()
        for i in range(h[v], h[v + 1]):
            u = d[i]
            if not c[u]:
                s.append(u)
                c[u] = True
    for i in range(n):
        if not c[i]: return i


import sys

read()
x = check(d1, h1)
if x != None:
    sys.stdout.write(f'NO\n1 {x + 1}')
    sys.exit(0)
x = check(d2, h2)
if x != None:
    sys.stdout.write(f'NO\n{x + 1} 1')
    sys.exit(0)
sys.stdout.write('YES')
