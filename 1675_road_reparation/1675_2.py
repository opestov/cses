import random, sys


class DSU:
    def __init__(self, n):
        self.p, self.r, self.z = list(range(n)), [0] * n, list(range(n))
        random.shuffle(self.z)

    def set(self, x):
        s, p = [], self.p
        while p[x] != x:
            s.append(x)
            x = p[x]
        for y in s:
            p[y] = x
        return x

    def union(self, a, b):
        p, r, z = self.p, self.r, self.z
        if r[a] < r[b] or (r[a] == r[b] and z[a] < z[b]):
            p[a] = p[b]
            r[b] += r[a] == r[b]
        else:
            p[b] = p[a]
            r[a] += r[a] == r[b]


E, M = 17, (1 << 17) - 1
n, m = map(int, sys.stdin.readline().split())
edges = [int(x) for x in sys.stdin.read().split()]
perm = [(edges[3 * i + 2] << E) | i for i in range(m)]
perm.sort()

dsu, acc, k = DSU(n), 0, 0
for p in perm:
    i = p & M
    u, v, w = edges[3 * i:3 * i + 3]
    a, b = dsu.set(u - 1), dsu.set(v - 1)
    if a != b:
        dsu.union(a, b)
        acc += w
        k += 1
        if k == n - 1:
            break
sys.stdout.write(str(acc) if k == n - 1 else 'IMPOSSIBLE')
