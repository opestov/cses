import collections, sys

n = int(sys.stdin.readline())
p = [int(x) - 1 for x in sys.stdin.readline().split()]

c = [0] * n
for x in p:
    c[x] += 1

q = collections.deque()
for i in range(n):
    if c[i] == 0:
        q.append(i)

r = [0] * n
while True:
    v = q.popleft()
    if v == 0: break

    u = p[v - 1]
    c[u] -= 1
    r[u] += r[v] + 1
    if c[u] == 0:
        q.append(u)
sys.stdout.write(' '.join(map(str, r)))
