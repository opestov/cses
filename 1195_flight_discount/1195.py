import sys, heapq


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

E, M = 18, (1 << 18) - 1

d, f = [-1] * (2 * n), [False] * (2 * n)
d[0] = 0

pq = [0]
for _ in range(2 * n):
    vv = heapq.heappop(pq) & M
    while f[vv]:
        vv = heapq.heappop(pq) & M
    f[vv] = True
    l, v = vv & 1, vv >> 1
    if v == n - 1:
        print(d[vv], file=sys.stdout)
        break

    for i in range(h[v], h[v + 1]):
        uu, w = (dest[i] << 1) | l, cost[i]
        if not f[uu] and (d[uu] == -1 or d[uu] > d[vv] + w):
            d[uu] = d[vv] + w
            heapq.heappush(pq, (d[uu] << E) | uu)
        uu += 1
        if l == 0 and not f[uu] and (d[uu] == -1 or d[uu] > d[vv] + (w // 2)):
            d[uu] = d[vv] + (w // 2)
            heapq.heappush(pq, (d[uu] << E) | uu)
