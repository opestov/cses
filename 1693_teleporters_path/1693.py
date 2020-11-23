import sys


class G:
    def __init__(self):
        n, m = map(int, sys.stdin.readline().split())
        a = [int(x) - 1 for x in sys.stdin.read().split()]
        d, h, inc = [0] * m, [0] * (n + 1), [0] * n
        for i in range(0, len(a), 2):
            u, v = a[i:i + 2]
            inc[v] += 1
            h[u] += 1
        for i in range(1, n + 1):
            h[i] += h[i - 1]
        for i in range(0, len(a), 2):
            u, v = a[i:i + 2]
            z = h[u] - 1
            d[z], h[u] = v, z
        self.n, self.m = n, m
        self.d, self.h, self.inc = d, h, inc

    def to(self, v, i):
        return self.d[self.h[v] + i]

    def ig(self, v):
        return self.inc[v]

    def og(self, v):
        return self.h[v + 1] - self.h[v]


def no():
    sys.stdout.write('IMPOSSIBLE')
    exit()


def test1():
    for i in range(1, n - 1):
        if g.ig(i) != g.og(i): no()
    if g.ig(0) + 1 != g.og(0) or g.og(n - 1) + 1 != g.ig(n - 1): no()


g = G()
n = g.n
test1()

s, p, r = [0], [0] * n, []
while len(s) > 0:
    v = s[-1]
    if p[v] == g.og(v):
        s.pop()
        r.append(str(v + 1))
        continue

    u, p[v] = g.to(v, p[v]), p[v] + 1
    s.append(u)

if len(r) != g.m + 1: no()
r.reverse()
sys.stdout.write(' '.join(r))
