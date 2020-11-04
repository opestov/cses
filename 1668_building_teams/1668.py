def gg():
    global e, h
    a = [int(x) - 1 for x in sys.stdin.read().split()]
    e, h = [0] * len(a), [0] * n
    for v in a:
        h[v] += 1
    for i in range(1, n):
        h[i] += h[i - 1]
    for i in range(0, len(a), 2):
        v, u = a[i], a[i + 1]
        h[v], h[u] = h[v] - 1, h[u] - 1
        e[h[v]], e[h[u]] = u, v
    h.append(len(a))


def doit():
    c = [0] * n
    s = []
    for i in range(n):
        if c[i] == 0:
            s.append(i)
            c[i] = 1
            while len(s) > 0:
                v = s.pop()
                for i in range(h[v], h[v + 1]):
                    u = e[i]
                    if c[u] == c[v]: return
                    if c[u] == 0:
                        c[u] = 3 - c[v]
                        s.append(u)
    return c


import sys

n, m = map(int, sys.stdin.readline().split())
gg()

r = doit()
if r is None:
    sys.stdout.write('IMPOSSIBLE')
else:
    sys.stdout.write(' '.join(map(str, r)))
