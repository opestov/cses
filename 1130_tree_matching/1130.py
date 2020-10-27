import collections, sys


def gg():
    E, M = 18, (1 << 18) - 1

    a = [int(x) - 1 for x in sys.stdin.read().split()]
    b = [(a[i] << E) | a[i ^ 1] for i in range(len(a))]
    b.sort()

    z = [-1] * (n)
    for i in range(len(a)):
        if i == 0 or (b[i] >> E) != (b[i - 1] >> E): z[b[i] >> E] = i
        a[i] = b[i] & M

    z.append(len(b))
    for i in range(n, -1, -1):
        if z[i] == -1: z[i] = z[i + 1]

    global e, h
    e, h = a, z


n = int(sys.stdin.readline())
gg()

c = [h[i + 1] - h[i] for i in range(n)]
q = collections.deque()
for i in range(n):
    if c[i] == 1:
        q.append(i)
q.pop()

r = 0
f = [True] * n
while len(q) > 0:
    v = q.popleft()
    c[v] = 0
    for i in range(h[v], h[v + 1]):
        u = e[i]
        if c[u] != 0:
            c[u] -= 1
            if f[v] and f[u]:
                r += 1
                f[v] = f[u] = False
            if c[u] <= 1: q.append(u)
print(r, file=sys.stdout)
