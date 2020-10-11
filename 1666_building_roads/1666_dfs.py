import sys

n, m = map(int, sys.stdin.readline().split())
aux = [int(x) for x in sys.stdin.read().split()]
g = {}
for i in range(0, len(aux), 2):
    a, b = aux[i], aux[i + 1]
    if a not in g: g[a] = [b]
    else: g[a].append(b)
    if b not in g: g[b] = [a]
    else: g[b].append(a)

color = [0] * (n + 1)


def dfs(v):
    c = v
    stack = [v]
    color[v] = c
    while len(stack) > 0:
        v = stack.pop()
        if v not in g: continue
        for u in g[v]:
            if color[u] == 0:
                stack.append(u)
                color[u] = c


a = []
for i in range(1, n + 1):
    if color[i] == 0:
        a.append(i)
        dfs(i)
print(len(a) - 1)
for i in range(1, len(a)):
    print(a[i - 1], a[i])
