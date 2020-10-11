import collections, sys
 
n, m = map(int, sys.stdin.readline().split())
g = sys.stdin.read().split()
f = [False] * ((n + 1) * (m + 2))
for r in range(n):
    for c in range(m):
        if g[r][c] == '.':
            f[r * (m + 2) + c + 1] = True
 
 
def bfs(c):
    q = collections.deque()
    q.append(c)
    f[c] = False
    while len(q) > 0:
        x = q.popleft()
        for y in [x - 1, x + 1, x - m - 2, x + m + 2]:
            if f[y]:
                q.append(y)
                f[y] = False
 
 
rooms = 0
for cell in range(len(f)):
    if f[cell]:
        rooms += 1
        bfs(cell)
print(rooms)

