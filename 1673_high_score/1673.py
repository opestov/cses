def gg():
    global n, m, a
    n, m = map(int, sys.stdin.readline().split())
    a = [int(x) for x in sys.stdin.read().split()]
    for i in range(0, len(a), 3):
        a[i], a[i + 1] = a[i] - 1, a[i + 1] - 1

    global dest, h
    dest, h = [0] * m, [0] * (n + 1)

    for i in range(1, len(a), 3):
        h[a[i]] += 1
    for i in range(1, n + 1):
        h[i] += h[i - 1]
    for i in range(0, len(a), 3):
        u, v = a[i], a[i + 1]
        h[v] -= 1
        dest[h[v]] = u


def main():
    f = [False] * n

    s = [n - 1]
    f[n - 1] = True
    nn = 0
    while len(s) > 0:
        v = s.pop()
        nn += 1
        for i in range(h[v], h[v + 1]):
            u = dest[i]
            if not f[u]:
                s.append(u)
                f[u] = True

    mm = 0
    for i in range(0, len(a), 3):
        if f[a[i]] and f[a[i + 1]]:
            a[mm:mm + 3] = a[i:i + 3]
            mm += 3

    _INF = -(10**13)
    d = [_INF] * n
    d[0] = 0
    for step in range(nn - 1):
        done = True
        for i in range(0, mm, 3):
            u, v, w = a[i:i + 3]
            if d[u] > _INF and d[v] < d[u] + w:
                done = False
                d[v] = d[u] + w
        if done: break

    for i in range(0, mm, 3):
        u, v, w = a[i:i + 3]
        if d[u] > _INF and d[v] < d[u] + w:
            sys.stdout.write('-1')
            return
    sys.stdout.write(str(d[n - 1]))


import sys

gg()
main()
