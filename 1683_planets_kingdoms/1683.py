def read():
    global n, m, d1, h1, d2, h2
    n, m = map(int, sys.stdin.readline().split())
    a = [int(x) - 1 for x in sys.stdin.read().split()]
    d1, h1, d2, h2 = [0] * m, [0] * (n + 1), [0] * m, [0] * (n + 1)
    for i in range(0, len(a), 2):
        h1[a[i]] += 1
        h2[a[i + 1]] += 1
    for i in range(1, n + 1):
        h1[i] += h1[i - 1]
        h2[i] += h2[i - 1]
    for i in range(0, len(a), 2):
        u, v = a[i:i + 2]
        d1[h1[u] - 1] = v
        h1[u] -= 1
        d2[h2[v] - 1] = u
        h2[v] -= 1


def dfs1():
    c, s, loc, r = [False] * n, [], [], []
    for i in range(n):
        if c[i]: continue
        c[i] = True
        s.append(i)
        loc.append(h1[i])
        while len(s) > 0:
            v, z = s[-1], loc[-1]
            if z == h1[v + 1]:
                s.pop()
                loc.pop()
                r.append(v)
                continue

            u, loc[-1] = d1[z], z + 1
            if not c[u]:
                c[u] = True
                s.append(u)
                loc.append(h1[u])
    r.reverse()
    return r


import sys

read()
order = dfs1()

color, k, s = [0] * n, 0, []
for x in order:
    if color[x] != 0: continue

    k += 1
    color[x] = k
    s.append(x)
    while len(s) > 0:
        v = s.pop()
        for i in range(h2[v], h2[v + 1]):
            u = d2[i]
            if color[u] == 0:
                color[u] = k
                s.append(u)

print(k, file=sys.stdout)
print(*color, file=sys.stdout)
