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
 
 
def dfs(x):
    d = [-1] * n
    s, d[x] = [x], 0
    y, dy = x, 0
    while len(s) > 0:
        v = s.pop()
        for i in range(h[v], h[v + 1]):
            u = e[i]
            if d[u] != -1: continue
            d[u] = d[v] + 1
            if d[u] > dy: y, dy = u, d[u]
            s.append(u)
    return y, dy
 
 
import sys
 
n = int(sys.stdin.readline())
gg()
 
v, _ = dfs(0)
_, r = dfs(v)
print(r, file=sys.stdout)

