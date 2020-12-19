class G():
    def __init__(self, n, a):
        dest, h = [0] * 2 * len(a), [0] * (n + 1)
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
        self.dest, self.h = dest, h


import sys

n = int(sys.stdin.readline())
c = [int(x) for x in sys.stdin.readline().split()]
g = G(n, [int(x) - 1 for x in sys.stdin.read().split()])

s, loc = [0], [g.h[0]]
p, cc, r = [0] * n, [set() for i in range(n)], [0] * n
cc[0].add(c[0])

while len(s) > 0:
    v, z = s[-1], loc[-1]
    if z == g.h[v + 1]:
        s.pop(), loc.pop()
        r[v] = len(cc[v])
        if v != 0:
            x, y = cc[v], cc[p[v]]
            if len(x) > len(y): x, y = y, x
            y.update(x)
            cc[p[v]] = y
        continue
    u, loc[-1] = g.dest[z], z + 1
    if p[v] == u: continue

    s.append(u), loc.append(g.h[u])
    p[u] = v
    cc[u].add(c[u])

sys.stdout.write(' '.join(map(str, r)))
