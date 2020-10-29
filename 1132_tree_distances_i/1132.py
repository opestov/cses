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


def doit():
    par, m1, m2 = [-1] * n, [-1] * n, [-1] * n
    flag = [False] * n

    s = [0]
    while len(s) > 0:
        v = s[-1]
        p = par[v]

        if flag[v]:
            s.pop()
            if v != 0:
                if m1[v] + 1 > m1[p]: m1[p], m2[p] = m1[v] + 1, m1[p]
                elif m1[v] + 1 > m2[p]: m2[p] = m1[v] + 1
            continue

        flag[v] = True
        for i in range(h[v], h[v + 1]):
            u = e[i]
            if u != p:
                par[u] = v
                s.append(u)

    up = [0] * n
    s.append(0)
    while len(s) > 0:
        v = s.pop()
        for i in range(h[v], h[v + 1]):
            u = e[i]
            if u != par[v]:
                up[u] = max(up[v] + 1,
                            (m2[v] if m1[v] == m1[u] + 1 else m1[v]) + 2)
                s.append(u)

    r = [] * n
    for i in range(n):
        r.append(str(max(up[i], m1[i] + 1)))
    sys.stdout.write(' '.join(r))


import sys

n = int(sys.stdin.readline())
gg()
doit()
