import collections, sys

n, m = map(int, sys.stdin.readline().split())
g = sys.stdin.read().split()
f = [False] * ((n + 1) * (m + 2))
for r in range(n):
    for c in range(m):
        id = r * (m + 2) + c + 1
        if g[r][c] != '#': f[id] = True
        if g[r][c] == 'A': a = id
        if g[r][c] == 'B': b = id

prev = [-1] * len(f)


def yes():
    path = []
    v = b
    while v != a:
        p = prev[v]
        if v == p - 1: path.append('L')
        if v == p + 1: path.append('R')
        if v == p - m - 2: path.append('U')
        if v == p + m + 2: path.append('D')
        v = p
    path.reverse()
    print('YES')
    print(len(path))
    print(*path, sep='')


queue = collections.deque()
queue.append(a)
prev[a] = a

while len(queue) > 0:
    u = queue.popleft()
    for v in [u - 1, u + 1, u - m - 2, u + m + 2]:
        if f[v] and prev[v] == -1:
            queue.append(v)
            prev[v] = u
            if v == b:
                yes()
                exit()

print('NO')
