class N():
    def __init__(self, n, m, a):
        self.flow, self.cap = [0] * 2 * m, [1] * 2 * m

        h, d, r = [0] * (n + 1), [0] * 2 * m, [0] * 2 * m
        for i in range(0, len(a), 2):
            h[a[i]] += 1
            h[a[i + 1]] += 1
        for i in range(1, n + 1):
            h[i] += h[i - 1]
        for i in range(0, len(a), 2):
            u, v = a[i:i + 2]
            p, q = h[u] - 1, h[v] - 1
            d[p], d[q] = v, u
            r[p], r[q] = q, p
            h[u], h[v] = p, q
        self.head, self.dest, self.re = h, d, r

    def inc(self, i):
        self.flow[i] += 1
        self.flow[self.re[i]] -= 1


def read():
    global n, g
    n, m = map(int, sys.stdin.readline().split())
    a = [int(x) - 1 for x in sys.stdin.read().split()]
    g = N(n, m, a)


def ff():
    f = [False] * n
    s, loc = [], []

    flag = True
    while flag:
        flag = False
        f[0] = True
        s.append(0), loc.append(g.head[0])
        while len(s) > 0:
            v, z = s[-1], loc[-1]
            if z == g.head[v + 1]:
                s.pop(), loc.pop()
                continue

            loc[-1] += 1
            u = g.dest[z]
            if not f[u] and g.cap[z] - g.flow[z] > 0:
                if u == n - 1: break
                f[u] = True
                s.append(u), loc.append(g.head[u])

        if len(s) > 0:
            flag = True
            for x in loc:
                g.inc(x - 1)
            s.clear(), loc.clear()
        for i in range(n):
            f[i] = False


def write():
    r = []
    acc = sum(g.flow[i] for i in range(g.head[0], g.head[1]))
    r.append(str(acc))

    a = [False] * n
    s, a[0] = [0], True
    while len(s) > 0:
        v = s.pop()
        for i in range(g.head[v], g.head[v + 1]):
            u = g.dest[i]
            if not a[u] and g.cap[i] > g.flow[i]:
                s.append(u)
                a[u] = True
    for v in range(n):
        if a[v]:
            for i in range(g.head[v], g.head[v + 1]):
                u = g.dest[i]
                if not a[u]:
                    r.append(f'{v + 1} {u + 1}')
    sys.stdout.write('\n'.join(r))


import sys

read()
ff()
write()
