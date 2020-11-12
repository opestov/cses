def read():
    global n, m, e, h, out
    n, m = map(int, sys.stdin.readline().split())
    a = [int(x) for x in sys.stdin.read().split()]
    e, h, out = [0] * m, [0] * (n + 1), [0] * n
    for i in range(0, len(a), 2):
        out[a[i] - 1] += 1
        h[a[i + 1] - 1] += 1
    for i in range(1, n + 1):
        h[i] += h[i - 1]
    for i in range(0, len(a), 2):
        u, v = a[i] - 1, a[i + 1] - 1
        h[v] -= 1
        e[h[v]] = u


import collections, sys

read()

q = collections.deque()
res, next = [0] * n, [0] * n
for i in range(n):
    if out[i] == 0: q.append(i)
res[n - 1] = 1

while len(q) > 0:
    v = q.popleft()
    for i in range(h[v], h[v + 1]):
        u = e[i]
        if res[v] != 0:
            if res[u] < res[v] + 1:
                res[u] = res[v] + 1
                next[u] = v
        out[u] -= 1
        if out[u] == 0: q.append(u)

r = []
if res[0] == 0:
    print('IMPOSSIBLE', file=sys.stdout)
else:
    v = 0
    while v != n - 1:
        r.append(v + 1)
        v = next[v]
    r.append(n)
    print(len(r), file=sys.stdout)
    print(*r, file=sys.stdout)
