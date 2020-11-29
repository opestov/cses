class N():
    def __init__(self, n, e):
        m = (len(e) // 3) * 2
        h = [0] * (n + 1)
        d, c, f, re = [0] * m, [0] * m, [0] * m, [0] * m
        for i in range(0, len(e), 3):
            h[e[i] - 1] += 1
            h[e[i + 1] - 1] += 1
        for i in range(1, n + 1):
            h[i] += h[i - 1]
        for i in range(0, len(e), 3):
            u, v, w = e[i] - 1, e[i + 1] - 1, e[i + 2]
            p, q = h[u] - 1, h[v] - 1
            d[p], c[p], re[p] = v, w, q
            d[q], re[q] = u, p
            h[u], h[v] = p, q
        self.ei, self.d, self.c, self.f, self.re = h, d, c, f, re

    def add(self, i, x):
        self.f[i] += x
        self.f[self.re[i]] -= x


def read():
    global n, g
    n, m = map(int, sys.stdin.readline().split())
    a = [int(x) for x in sys.stdin.read().split()]
    g = N(n, a)


def ff():
    ei, dest, flow, cap = g.ei, g.d, g.f, g.c
    f, s, loc = [False] * n, [], []

    x = 2**40
    while x > 0:

        f[0] = True
        s.append(0), loc.append(ei[0])
        while len(s) > 0:
            v, z = s[-1], loc[-1]
            if z == ei[v + 1]:
                s.pop(), loc.pop()
                continue
            u, c, loc[-1] = dest[z], cap[z] - flow[z], z + 1
            if not f[u] and c >= x:
                if u == n - 1: break
                f[u] = True
                s.append(u), loc.append(ei[u])
        if len(loc) > 0:
            for i in loc:
                g.add(i - 1, x)
        else:
            x //= 2

        for i in range(n):
            f[i] = False
        s.clear(), loc.clear()


import sys

read()
ff()
sys.stdout.write(str(sum(g.f[i] for i in range(g.ei[0], g.ei[1]))))
