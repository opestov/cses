class G:
    def __init__(self, n, e):
        d, h = [0] * (len(e) // 2), [0] * (n + 1)
        for i in range(0, len(e), 2):
            h[e[i]] += 1
        for i in range(1, n + 1):
            h[i] += h[i - 1]
        for i in range(0, len(e), 2):
            u, v = e[i:i + 2]
            p = h[u] - 1
            d[p], h[u] = v, p
        self.n, self.d, self.h = n, d, h

    def eb(self, v):
        return self.h[v]

    def ee(self, v):
        return self.h[v + 1]

    def dest(self, i):
        return self.d[i]


class Builder:
    def __init__(self, n, m):
        self.e, self.i, self.n = [0] * (2 * m), 0, n

    def add(self, u, v):
        self.n = max(self.n, u + 1, v + 1)
        self.e[self.i], self.e[self.i + 1] = u, v
        self.i += 2

    def build(self):
        return G(self.n, self.e)


def read():
    global n, g1, g2
    m, n = map(int, sys.stdin.readline().split())
    a = sys.stdin.read().split()
    b1, b2 = Builder(2 * n, 2 * m), Builder(2 * n, 2 * m)
    for i in range(0, len(a), 4):
        u = 2 * (int(a[i + 1]) - 1)
        if a[i] == '-': u += 1
        v = 2 * (int(a[i + 3]) - 1)
        if a[i + 2] == '-': v += 1
        b1.add(u ^ 1, v)
        b1.add(v ^ 1, u)
        b2.add(v, u ^ 1)
        b2.add(u, v ^ 1)
    g1, g2 = b1.build(), b2.build()


def condense():
    global c, ts
    c, ts = [0] * (2 * n), []

    s, loc, o = [], [], []
    for i in range(2 * n):
        if c[i] == 1: continue
        c[i] = 1
        s.append(i)
        loc.append(g1.eb(i))
        while len(s) > 0:
            v, z = s[-1], loc[-1]
            if z == g1.ee(v):
                o.append(v)
                s.pop()
                loc.pop()
                continue
            u, loc[-1] = g1.dest(z), z + 1
            if c[u] == 0:
                c[u] = 1
                s.append(u)
                loc.append(g1.eb(u))
    o.reverse()

    for i in range(2 * n):
        c[i] = -1
    for x in o:
        if c[x] != -1: continue
        ts.append(x)
        s.append(x)
        c[x] = x
        while len(s) > 0:
            v = s.pop()
            for i in range(g2.eb(v), g2.ee(v)):
                u = g2.dest(i)
                if c[u] == -1:
                    s.append(u)
                    c[u] = x
    ts.reverse()


def no():
    for i in range(n):
        if c[2 * i] == c[2 * i + 1]:
            sys.stdout.write('IMPOSSIBLE')
            exit()


def yes():
    s = []
    r = [-1] * n
    for x in ts:
        if r[x >> 1] != -1: continue

        s.append(x)
        r[x >> 1] = x & 1
        while len(s) > 0:
            v = s.pop()
            for i in range(g1.eb(v), g1.ee(v)):
                u = g1.dest(i)
                if r[u >> 1] == -1:
                    s.append(u)
                    r[u >> 1] = u & 1
    sys.stdout.write(' '.join(map(lambda x: '+' if x == 0 else '-', r)))


import sys

read()
condense()
no()
yes()
