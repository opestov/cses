import sys


def gg():
    global n, m, dest, cost, h
    n, m = map(int, sys.stdin.readline().split())
    dest, cost, h = [0] * m, [0] * m, [0] * (n + 1)

    a = [int(x) for x in sys.stdin.read().split()]
    for i in range(0, len(a), 3):
        h[a[i] - 1] += 1
    for i in range(1, n + 1):
        h[i] += h[i - 1]
    for i in range(0, len(a), 3):
        u, v, w = a[i:i + 3]
        j = h[u - 1] - 1
        dest[j], cost[j] = v - 1, w
        h[u - 1] -= 1


gg()

import heapq

E, M = 17, (1 << 17) - 1

d, f = [-1] * n, [False] * n
d[0] = 0

pq = [0]
for _ in range(n):
    v = heapq.heappop(pq) & M
    while f[v]:
        v = heapq.heappop(pq) & M
    f[v] = True

    for i in range(h[v], h[v + 1]):
        u, w = dest[i], cost[i]
        if not f[u] and (d[u] == -1 or d[u] > d[v] + w):
            d[u] = d[v] + w
            heapq.heappush(pq, (d[u] << 17) | u)
print(*d, file=sys.stdout)
