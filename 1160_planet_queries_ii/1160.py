import sys

n, q = map(int, sys.stdin.readline().split())
t = [int(x) - 1 for x in sys.stdin.readline().split()]
a = [int(x) - 1 for x in sys.stdin.read().split()]

acc = 0
c, e, d, o, cyc = [-1] * n, list(range(n)), [0] * n, [-1] * n, []
for x in range(n):
    if c[x] != -1: continue
    s, c[x], y = [x], acc, t[x]
    while c[y] == -1:
        s.append(y)
        c[y], y = acc, t[y]
    ns = len(s)

    if c[y] == acc:
        k = s.index(y)
        for i in range(k):
            e[s[i]], d[s[i]] = y, k - i
        for i in range(k, ns):
            o[s[i]] = i - k
        cyc.append(ns - k)
        acc += 1
    else:
        for i in range(ns):
            c[s[i]], d[s[i]], e[s[i]] = c[y], d[y] + ns - i, e[y]

d2 = [t]
for i in range(18):
    s = d2[-1]
    d2.append([s[s[x]] for x in range(n)])

r = []
for i in range(0, len(a), 2):
    u, v = a[i:i + 2]
    if u == v: r.append('0')
    elif c[u] != c[v] or d[u] < d[v]: r.append('-1')
    elif d[v] == 0:
        extra = d[u]
        if d[u] > 0: u = e[u]
        z = o[v] - o[u]
        if z < 0: z += cyc[c[u]]
        r.append(str(extra + z))
    elif d[u] == d[v]:
        r.append('-1')
    else:
        z, x, j = d[u] - d[v], u, 0
        while z > 0:
            if z & 1: x = d2[j][x]
            z, j = z >> 1, j + 1
        if x == v:
            r.append(str(d[u] - d[v]))
        else:
            r.append('-1')
sys.stdout.write('\n'.join(r))
