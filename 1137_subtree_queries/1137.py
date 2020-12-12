class G():
    def __init__(self, n, a):
        dest, h = [0] * (2 * n - 2), [0] * (n + 1)
        for i in range(0, len(a), 2):
            u, v = a[i] - 1, a[i + 1] - 1
            h[u], h[v] = h[u] + 1, h[v] + 1
        for i in range(1, n + 1):
            h[i] += h[i - 1]
        for i in range(0, len(a), 2):
            u, v = a[i] - 1, a[i + 1] - 1
            p, q = h[u] - 1, h[v] - 1
            dest[p], dest[q] = v, u
            h[u], h[v] = p, q
        self.n, self.dest, self.h = n, dest, h


class F():
    def __init__(self, g):
        n = g.n
        par, a, b = [0] * n, [0] * n, [0] * n
        s, loc, arr = [0], [g.h[0]], [0]
        while len(s) > 0:
            v, z = s[-1], loc[-1]
            if z == g.h[v + 1]:
                s.pop(), loc.pop()
                arr.append(v)
                b[v] = len(arr) - 1
                continue
            u, loc[-1] = g.dest[z], z + 1
            if u != par[v]:
                s.append(u), loc.append(g.h[u])
                arr.append(u)
                a[u] = len(arr) - 1
                par[u] = v
        self.a, self.b, self.arr = a, b, arr


class S():
    def __init__(self, n):
        p2 = 1
        while p2 < n:
            p2 *= 2
        self.t, self.p2 = [0] * (2 * p2), p2

    def sum(self, a, b):
        t, a, b = self.t, a + self.p2, b + self.p2
        acc = 0
        while a <= b:
            if a & 1: acc, a = acc + t[a], a + 1
            if (b & 1) == 0: acc, b = acc + t[b], b - 1
            a, b = a // 2, b // 2
        return acc

    def change(self, i, x):
        t, i = self.t, i + self.p2
        delta = x - t[i]
        while i > 0:
            t[i] += delta
            i //= 2


import sys

n, q = map(int, sys.stdin.readline().split())
v = [int(x) for x in sys.stdin.readline().split()]
a = [int(x) for x in sys.stdin.read().split()]
g = G(n, a[:2 * (n - 1)])
f = F(g)
s = S(len(f.arr))

for i in range(n):
    s.change(f.a[i], v[i])

res = []
i = 2 * n - 2
while i < len(a):
    v = a[i + 1] - 1
    if a[i] == 1:
        s.change(f.a[v], a[i + 2])
        i += 3
    else:
        res.append(str(s.sum(f.a[v], f.b[v])))
        i += 2
sys.stdout.write('\n'.join(res))
