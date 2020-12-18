class G():
    def __init__(self, n, a):
        dest, h = [0] * (2 * len(a)), [0] * (n + 1)
        for i in range(0, len(a), 2):
            u, v = a[i:i + 2]
            h[u], h[v] = h[u] + 1, h[v] + 1
        for i in range(1, n + 1):
            h[i] += h[i - 1]
        for i in range(0, len(a), 2):
            u, v = a[i:i + 2]
            p, q = h[u] - 1, h[v] - 1
            dest[p], dest[q] = v, u
            h[u], h[v] = p, q
        self.n, self.dest, self.h = n, dest, h


class D():
    def __init__(self, n):
        self.p = list(range(n))

    def top(self, x):
        p, y = self.p, x
        while p[x] != x:
            x = p[x]
        while y != x:
            p[y], y = x, p[y]
        return x

    def append(self, p, x):
        self.p[x] = p


def main():
    ts = []
    op, cl, saddle, p = [0] * n, [0] * n, [0] * n, [-1] * n

    s, loc = [0], [g1.h[0]]
    p[0] = 0
    while len(s) > 0:
        v, z = s[-1], loc[-1]
        if z == g1.h[v + 1]:
            s.pop(), loc.pop()
            if v != 0:
                dsu.append(p[v], v)
            ts.append(v)
            continue

        u, loc[-1] = g1.dest[z], z + 1
        if p[v] == u: continue

        s.append(u)
        loc.append(g1.h[u])
        p[u] = v

        for i in range(g2.h[u], g2.h[u + 1]):
            w = g2.dest[i]
            if p[w] != -1:
                a = dsu.top(w)
                op[u] += 1
                cl[a] += 1
                if a != w:
                    saddle[a] += 1
                    op[w] += 1
                    cl[a] += 1

    ans, up = [0] * n, [0] * n
    for v in ts:
        up[v] += op[v] - cl[v]
        ans[v] += op[v] - saddle[v]
        if v:
            up[p[v]] += up[v]
            ans[p[v]] += up[v]

    sys.stdout.write(' '.join(map(str, ans)))


import sys

n, q = map(int, sys.stdin.readline().split())
a = [int(x) - 1 for x in sys.stdin.read().split()]
g1 = G(n, a[:2 * (n - 1)])
g2 = G(n, a[2 * (n - 1):])
dsu = D(n)

main()
