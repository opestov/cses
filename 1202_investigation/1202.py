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

M = 10**9 + 7
n, m = map(int, sys.stdin.readline().split())
a = [int(x) for x in sys.stdin.read().split()]
g = G(n, m, a)

di, nu, mi, ma = [-1] * n, [0] * n, [n] * n, [0] * n
di[0], nu[0], mi[0], ma[0] = 0, 1, 0, 0

f = [False] * n
pq = [(0, 0)]
while True:
    dv, v = heapq.heappop(pq)
    while f[v]:
        dv, v = heapq.heappop(pq)
    f[v] = True
    if v == n - 1: break

    for i in range(g.h[v], g.h[v + 1]):
        u, w = g.dest[i], g.cost[i]
        if f[u]: continue
        if di[u] == -1 or di[u] > dv + w:
            heapq.heappush(pq, (dv + w, u))
            di[u], nu[u], mi[u], ma[u] = dv + w, nu[v], mi[v] + 1, ma[v] + 1
        elif di[u] == dv + w:
            nu[u] += nu[v]
            if nu[u] >= M: nu[u] -= M
            mi[u], ma[u] = min(mi[u], mi[v] + 1), max(ma[u], ma[v] + 1)

print(di[n - 1], nu[n - 1], mi[n - 1], ma[n - 1], file=sys.stdout)
