def read():
    global n, m, coins, d1, h1, d2, h2
    n, m = map(int, sys.stdin.readline().split())
    coins = [int(x) for x in sys.stdin.readline().split()]
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


def condense():
    order = dfs1()

    global w
    color, k, s, w = [-1] * n, 0, [], []

    for x in order:
        if color[x] != -1: continue

        w.append(coins[x])
        color[x] = k
        s.append(x)
        while len(s) > 0:
            v = s.pop()
            for i in range(h2[v], h2[v + 1]):
                u = d2[i]
                if color[u] == -1:
                    color[u] = k
                    w[-1] += coins[u]
                    s.append(u)
        k += 1

    global d, h, acc
    h, acc = [0] * (k + 1), [0] * k
    for i in range(n):
        v = color[i]
        for j in range(h1[i], h1[i + 1]):
            u = color[d1[j]]
            if v != u:
                h[u] += 1
                acc[v] += 1
    for i in range(1, k + 1):
        h[i] += h[i - 1]
    d = [0] * h[k]
    for i in range(n):
        v = color[i]
        for j in range(h1[i], h1[i + 1]):
            u = color[d1[j]]
            if v != u:
                z = h[u] - 1
                d[z] = v
                h[u] = z


import collections, sys

read()
condense()

q, ans = collections.deque(), [0] * len(w)
for i in range(len(acc)):
    if acc[i] == 0: q.append(i)
while len(q) > 0:
    v = q.popleft()
    ans[v] += w[v]
    for i in range(h[v], h[v + 1]):
        u = d[i]
        ans[u] = max(ans[u], ans[v])
        acc[u] -= 1
        if acc[u] == 0:
            q.append(u)

print(max(ans), file=sys.stdout)
