def gg():
    global e, h
    a = [int(x) - 1 for x in sys.stdin.read().split()]
    e, h = [0] * len(a), [0] * n
    for v in a:
        h[v] += 1
    for i in range(1, n):
        h[i] += h[i - 1]
    for i in range(0, len(a), 2):
        v, u = a[i], a[i + 1]
        h[v], h[u] = h[v] - 1, h[u] - 1
        e[h[v]], e[h[u]] = u, v
    h.append(len(a))


def bfs():
    d, p = [-1] * n, [-1] * n

    q = collections.deque()
    q.append(0)
    d[0] = 0

    while len(q) > 0 and d[n - 1] == -1:
        v = q.popleft()
        for i in range(h[v], h[v + 1]):
            u = e[i]
            if d[u] != -1: continue
            d[u], p[u] = d[v] + 1, v
            q.append(u)

    if d[n - 1] == -1:
        print('IMPOSSIBLE', file=sys.stdout)
        return

    print(d[n - 1] + 1, file=sys.stdout)
    r = []
    v = n - 1
    while v != -1:
        r.append(v + 1)
        v = p[v]
    r.reverse()
    print(*r, file=sys.stdout)


import collections, sys

n, m = map(int, sys.stdin.readline().split())
gg()
bfs()
