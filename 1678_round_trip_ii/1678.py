def gg():
    global e, h
    a = [int(x) - 1 for x in sys.stdin.read().split()]
    e, h = [0] * len(a), [0] * (n + 1)
    for i in range(0, len(a), 2):
        h[a[i]] += 1
    for i in range(1, n + 1):
        h[i] += h[i - 1]
    for i in range(0, len(a), 2):
        v, u = a[i], a[i + 1]
        h[v] = h[v] - 1
        e[h[v]] = u


def dfs():
    c = [0] * n
    s, m = [], []

    for i in range(n):
        if c[i] != 0: continue

        s.append(i)
        m.append(h[i])
        while len(s) > 0:
            v, k = s[-1], m[-1]
            if k == h[v]: c[v] = 1
            if k == h[v + 1]:
                c[v] = 2
                s.pop()
                m.pop()
                continue

            u = e[k]
            m[-1] += 1
            if c[u] == 0:
                s.append(u)
                m.append(h[u])
            elif c[u] == 1:
                s.append(u)
                return s[s.index(u):]


import sys

n, m = map(int, sys.stdin.readline().split())
gg()

r = dfs()
if r is None:
    print('IMPOSSIBLE', file=sys.stdout)
else:
    print(len(r), ' '.join([str(x + 1) for x in r]), sep='\n', file=sys.stdout)
