def read():
    global n, m, d, h, re
    n, m = map(int, sys.stdin.readline().split())
    a = [int(x) - 1 for x in sys.stdin.read().split()]
    d, re, h = [0] * (2 * m), [0] * (2 * m), [0] * (n + 1)
    for i in range(0, len(a), 2):
        h[a[i]] += 1
        h[a[i + 1]] += 1
    for i in range(1, n + 1):
        h[i] += h[i - 1]
    for i in range(0, len(a), 2):
        v, u = a[i:i + 2]
        p, q = h[v] - 1, h[u] - 1
        d[p], re[p] = u, q
        d[q], re[q] = v, p
        h[v], h[u] = p, q


import sys

read()
for x in h:
    if x % 2 != 0:
        sys.stdout.write('IMPOSSIBLE')
        sys.exit(0)

rm = [False] * (2 * m)

s, p, r = [0], h[:], []
while len(s) > 0:
    v = s[-1]
    if p[v] == h[v + 1]:
        r.append(v + 1)
        s.pop()
        continue

    e = p[v]
    u = d[e]
    p[v] += 1
    if not rm[e]:
        rm[e], rm[re[e]] = True, True
        s.append(u)

if len(r) == m + 1:
    print(*r, file=sys.stdout)
else:
    sys.stdout.write('IMPOSSIBLE')
