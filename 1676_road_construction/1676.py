import random, sys


class DSU:
    def __init__(self, n):
        self.r, self.k = [0] * n, [1] * n
        self.p, self.z = list(range(n)), list(range(n))
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
        p, r, k, z = self.p, self.r, self.k, self.z
        if r[a] < r[b] or (r[a] == r[b] and z[a] < z[b]):
            p[a], k[b], r[b] = b, k[b] + k[a], r[b] + (r[a] == r[b])
            return k[b]
        p[b], k[a], r[a] = a, k[a] + k[b], r[a] + (r[a] == r[b])
        return k[a]


n, m = map(int, sys.stdin.readline().split())
edges = [int(x) for x in sys.stdin.read().split()]

dsu, k, sz = DSU(n), n, 0
r = []
for i in range(0, len(edges), 2):
    u, v = edges[i] - 1, edges[i + 1] - 1
    a, b = dsu.set(u), dsu.set(v)
    print('z', a, b)
    if a != b:
        k -= 1
        sz = max(sz, dsu.union(a, b))
    r.append("%d %d" % (k, sz))
sys.stdout.write('\n'.join(r))
