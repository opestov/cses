import sys


class G():
    def __init__(self):
        n = int(sys.stdin.readline())
        m = 2 * (n - 1)
        a = [int(x) - 1 for x in sys.stdin.read().split()]
        dest, h = [0] * m, [0] * (n + 1)
        for i in range(0, len(a), 2):
            h[a[i]] += 1
            h[a[i + 1]] += 1
        for i in range(1, n + 1):
            h[i] += h[i - 1]
        for i in range(0, len(a), 2):
            v, u = a[i:i + 2]
            p, q = h[v] - 1, h[u] - 1
            dest[p], dest[q] = u, v
            h[v], h[u] = p, q
        self.n, self.dest, self.h = n, dest, h


g = G()
n = g.n
size, par, ans, flag = [0] * n, [0] * n, [0] * n, [False] * n

s, tsort = [], []
for i in range(g.h[0], g.h[1]):
    u = g.dest[i]
    s.append(u)
    par[u], size[u] = 0, 1

while len(s) > 0:
    v = s[-1]
    p = par[v]
    if flag[v]:
        s.pop()
        size[p] += size[v]
        ans[p] += ans[v] + size[v]
        tsort.append(v)
        continue

    flag[v] = True
    for i in range(g.h[v], g.h[v + 1]):
        u = g.dest[i]
        if u != p:
            s.append(u)
            par[u], size[u] = v, 1

tsort.reverse()
for v in tsort:
    p = par[v]
    ans[v] = ans[p] + (n - 2 * size[v])
sys.stdout.write(' '.join(map(str, ans)))
