import bisect


class Ones:
    def __init__(self, n):
        p2 = 1
        while p2 < n:
            p2 *= 2
        t = [-1] * (2 * p2)
        for i in range(n):
            t[p2 + i] = i
        for i in range(p2 - 1, 0, -1):
            t[i] = max(t[2 * i], t[2 * i + 1])

        self.t, self.p2 = t, p2

    def max_leq(self, i):
        i = self.p2 + i
        while self.t[i] == -1:
            if i & -i == i: break
            if i & 1: i //= 2
            else: i -= 1
        return self.t[i]

    def remove(self, i):
        t, j = self.t, self.p2 + i
        t[j] = -1
        j //= 2
        while t[j] == i:
            t[j] = max(t[2 * j], t[2 * j + 1])
            j //= 2


n, m = map(int, input().split())

h = [int(x) for x in input().split()]
h.sort()

t = [int(x) for x in input().split()]

ones = Ones(n)
res = [-1] * m
for i in range(m):
    j = bisect.bisect(h, t[i])
    if j == n or h[j] > t[i]: j -= 1
    if j == -1: continue

    j = ones.max_leq(j)
    if j == -1: continue

    res[i] = h[j]
    ones.remove(j)

print(*res, sep='\n')
