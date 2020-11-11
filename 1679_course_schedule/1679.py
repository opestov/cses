def read_data():
    global n, m, dest, h
    n, m = map(int, sys.stdin.readline().split())
    a = [int(x) for x in sys.stdin.read().split()]
    dest, h = [0] * m, [0] * (n + 1)
    for i in range(0, len(a), 2):
        h[a[i] - 1] += 1
    for i in range(1, n + 1):
        h[i] += h[i - 1]
    for i in range(0, len(a), 2):
        u, v = a[i] - 1, a[i + 1] - 1
        h[u] -= 1
        dest[h[u]] = v


def dfs():
    c = [0] * n
    s, z, r = [], [], []

    for i in range(n):
        if c[i] != 0: continue
        s.append(i)
        z.append(h[i])
        while len(s) > 0:
            v, k = s[-1], z[-1]
            if k == h[v]: c[v] = 1
            if k == h[v + 1]:
                s.pop()
                z.pop()
                c[v] = 2
                r.append(str(v + 1))
                continue

            u = dest[k]
            z[-1] += 1
            if c[u] == 1: return
            if c[u] == 0:
                s.append(u)
                z.append(h[u])
    r.reverse()
    return r


import sys

read_data()
r = dfs()
if r is None:
    sys.stdout.write('IMPOSSIBLE')
else:
    sys.stdout.write(' '.join(r))
