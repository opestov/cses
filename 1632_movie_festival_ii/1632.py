import bisect, sys


class Projector:
    def __init__(self, domain):
        self.aux = domain[:]
        self.aux.sort()

        i = 0
        while i + 1 < len(self.aux) and self.aux[i] == self.aux[i + 1]:
            i += 1

        k = i
        for i in range(k + 1, len(domain)):
            if self.aux[k] != self.aux[i]:
                k += 1
                self.aux[k] = self.aux[i]
        self.n = k + 1

    def project(self, x):
        return bisect.bisect_left(self.aux, x, 0, self.n)


class Collection:
    def __init__(self, domain_size):
        n = 1
        while n < domain_size:
            n *= 2
        self.n = n
        self.quantity = [0] * domain_size
        self.largest = [-1] * (2 * n)

    def add(self, i, cnt=1):
        self.quantity[i] += cnt
        j = i + self.n
        while j > 0 and self.largest[j] < i:
            self.largest[j] = i
            j //= 2

    def remove(self, i):
        self.quantity[i] -= 1
        if self.quantity[i] > 0:
            return
        self.largest[i + self.n] = -1
        j = (i + self.n) // 2
        while j > 0 and self.largest[j] == i:
            self.largest[j] = max(self.largest[2 * j], self.largest[2 * j + 1])
            j //= 2

    def max_leq(self, x):
        i = x + self.n
        while i > 0:
            if self.largest[i] != -1:
                return self.largest[i]
            if i & -i == i: break
            i = (i - 1) // 2
        return -1


n, k = map(int, sys.stdin.readline().split())
a = [int(x) for x in sys.stdin.read().split()]

proj = Projector(a)

for i in range(2 * n):
    a[i] = proj.project(a[i])

p = list(range(n))
p.sort(key=lambda i: a[2 * i + 1])

c = Collection(proj.n)
c.add(0, k)

ans = 0
for i in p:
    x, y = a[2 * i], a[2 * i + 1]
    z = c.max_leq(x)
    if z != -1:
        c.remove(z)
        c.add(y)
        ans += 1

print(ans)
