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

M = 7 + 10**9
read()

q = collections.deque()
res = [0] * n
for i in range(n):
    if out[i] == 0: q.append(i)
res[n - 1] = 1

while len(q) > 0:
    v = q.popleft()
    for i in range(h[v], h[v + 1]):
        u = e[i]
        res[u] = (res[u] + res[v]) % M
        out[u] -= 1
        if out[u] == 0: q.append(u)
sys.stdout.write(str(res[0]))
