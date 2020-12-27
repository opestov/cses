class G():
    def __init__(self, n, m, a):
        dest, cost, h = [0] * m, [0] * m, [0] * (n + 1)
        for i in range(0, len(a), 3):
            h[a[i] - 1] += 1
        for i in range(1, n + 1):
            h[i] += h[i - 1]
        for i in range(0, len(a), 3):
            u, v, w = a[i] - 1, a[i + 1] - 1, a[i + 2]
            j = h[u] - 1
            dest[j], cost[j] = v, w
            h[u] = j
        self.dest, self.cost, self.h = dest, cost, h


import heapq, sys

n, m, k = map(int, sys.stdin.readline().split())
a = [int(x) for x in sys.stdin.read().split()]
g = G(n, m, a)

r = []
f, pq = [0] * n, [(0, 0)]
while True:
    dv, v = heapq.heappop(pq)
    while f[v] == k:
        dv, v = heapq.heappop(pq)
    f[v] += 1
    if v == n - 1:
        r.append(str(dv))
        if f[v] == k: break

    for i in range(g.h[v], g.h[v + 1]):
        u, w = g.dest[i], g.cost[i]
        if f[u] < k: heapq.heappush(pq, (dv + w, u))
sys.stdout.write(' '.join(r))
