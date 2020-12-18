class G():
    def __init__(self, n, a):
        dest, h = [0] * len(a), [0] * (n + 1)
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
        o, x, y = [0], [0] * g.n, [0] * g.n
        s, loc, p = [0], [g.h[0]], [0] * g.n
        while len(s) > 0:
            v, z = s[-1], loc[-1]
            if g.h[v + 1] == z:
                s.pop(), loc.pop()
                y[v] = len(o) - 1
                continue

            u, loc[-1] = g.dest[z], z + 1
            if p[v] == u: continue

            x[u] = len(o)
            o.append(u)

            s.append(u)
            loc.append(g.h[u])
            p[u] = v
        self.o, self.x, self.y = o, x, y


class T():
    def __init__(self, n):
        self.t = [0] * (n + 1)

    def add(self, i, j, x):
        t = self.t
        i += 1
        while i < len(t):
            t[i] += x
            i = i + (-i & i)
        i = j + 2
        while i < len(t):
            t[i] -= x
            i = i + (-i & i)

    def val(self, i):
        t, i, acc = self.t, i + 1, 0
        while i > 0:
            i, acc = i & (i - 1), acc + t[i]
        return acc


import sys

n, q = map(int, sys.stdin.readline().split())
v = [int(x) for x in sys.stdin.readline().split()]
a = [int(x) for x in sys.stdin.read().split()]
g = G(n, a[:2 * n - 2])
f = F(g)

t = T(n)
for i in range(n):
    t.add(f.x[i], f.y[i], v[i])

r = []
i = 2 * n - 2
while i < len(a):
    q = a[i + 1] - 1
    if a[i] == 1:
        x, i = a[i + 2], i + 1
        delta, v[q] = x - v[q], x
        t.add(f.x[q], f.y[q], delta)
    else:
        r.append(str(t.val(f.x[q])))
    i += 2

sys.stdout.write('\n'.join(r))
