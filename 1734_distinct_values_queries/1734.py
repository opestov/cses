class F():
    def __init__(self, n):
        self.t = [0] * (n + 1)

    def add(self, i, x):
        t, i = self.t, i + 1
        while i < len(t):
            t[i] += x
            i += -i & i

    def sum(self, i):
        t, acc, i = self.t, 0, i + 1
        while i:
            acc += t[i]
            i &= i - 1
        return acc


import sys

n, q = map(int, sys.stdin.readline().split())
a = [int(x) for x in sys.stdin.readline().split()]

b = [int(x) - 1 for x in sys.stdin.read().split()]
o, h = [0] * q, [0] * (n + 1)
for i in range(0, 2 * q, 2):
    h[b[i + 1]] += 1
for i in range(1, n + 1):
    h[i] += h[i - 1]
for i in range(0, 2 * q, 2):
    p = h[b[i + 1]] - 1
    o[p] = i
    h[b[i + 1]] = p

f = F(n)

r = [None] * q
d = {}
j = 0
for i in o:
    x, y = b[i], b[i + 1]
    while j <= y:
        z = d.get(a[j])
        if z is not None: f.add(z, -1)
        f.add(j, 1)
        d[a[j]] = j
        j += 1
    r[i // 2] = str(f.sum(y) - f.sum(x - 1))

sys.stdout.write('\n'.join(r))
