import sys

n, m, k = map(int, sys.stdin.readline().split())
a = [int(x) - 1 for x in sys.stdin.read().split()]
d, h = [0] * k, [0] * (n + 1)
for i in range(0, len(a), 2):
    h[a[i]] += 1
for i in range(1, n + 1):
    h[i] += h[i - 1]
for i in range(0, len(a), 2):
    p = h[a[i]] - 1
    d[p] = a[i + 1]
    h[a[i]] = p

g, b = [-1] * n, [-1] * m

vis = [False] * n
flag = True
while flag:
    for i in range(n):
        vis[i] = False
    flag = False

    for x in range(n):
        if g[x] != -1: continue
        s, loc, vis[x] = [x], [h[x]], True
        while len(s) > 0:
            v, z = s[-1], loc[-1]
            if z == h[v + 1]:
                s.pop()
                loc.pop()
                continue
            u, loc[-1] = b[d[z]], z + 1
            if u == -1: break
            if not vis[u]:
                s.append(u)
                loc.append(h[u])
                vis[u] = True

        for i in range(len(s)):
            u, v = s[i], d[loc[i] - 1]
            g[u], b[v] = v, u
        flag = flag or len(s) > 0

r = []
for i in range(n):
    if g[i] != -1: r.append(f'{i+1} {g[i] + 1}')
sys.stdout.write(f'{len(r)}\n')
sys.stdout.write('\n'.join(r))
