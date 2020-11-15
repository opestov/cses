def read():
    global n, m, dest, cost, h
    n, m = map(int, sys.stdin.readline().split())
    dest, cost, h = [0] * (2 * m), [0] * (2 * m), [0] * (n + 1)

    a = [int(x) for x in sys.stdin.read().split()]
    for i in range(0, len(a), 3):
        h[a[i] - 1] += 1
        h[a[i + 1] - 1] += 1
    for i in range(1, n + 1):
        h[i] += h[i - 1]
    for i in range(0, len(a), 3):
        u, v, w = a[i:i + 3]
        j = h[u - 1] - 1
        dest[j], cost[j] = v - 1, w
        h[u - 1] = j
        j = h[v - 1] - 1
        dest[j], cost[j] = u - 1, w
        h[v - 1] = j


import sys, heapq

read()

E, M = 17, (1 << 17) - 1

d, f = [-1] * n, [False] * n
d[0] = 0

pq = [0]
for _ in range(n):
    while len(pq) > 0 and f[pq[0] & M]:
        heapq.heappop(pq)
    if len(pq) == 0:
        sys.stdout.write('IMPOSSIBLE')
        sys.exit(0)
    v = heapq.heappop(pq) & M
    f[v] = True

    for i in range(h[v], h[v + 1]):
        u, w = dest[i], cost[i]
        if not f[u] and (d[u] == -1 or d[u] > w):
            d[u] = w
            heapq.heappush(pq, (d[u] << 17) | u)
print(sum(d), file=sys.stdout)
