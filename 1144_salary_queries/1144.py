class Ones:
    def __init__(self, n):
        p2 = 1
        while p2 < n:
            p2 *= 2
        self.t = [0] * (2 * p2)
        self.p2 = p2

    def __add(self, i, delta):
        p2, t = self.p2, self.t
        i += p2
        while i > 0:
            t[i] += delta
            i //= 2

    def __le(self, i):
        p2, t = self.p2, self.t
        i, acc = i + p2, 0
        while True:
            if i == 1 or i % 2 == 0: acc += t[i]
            if i & -i == i: break
            i = (i - 1) // 2
        return acc

    def inc(self, i):
        self.__add(i, 1)

    def dec(self, i):
        self.__add(i, -1)

    def count(self, a, b):
        return self.__le(b) - (0 if a == 0 else self.__le(a - 1))


import sys


def int1(x):
    if x == '!': return 1
    if x == '?': return 2
    return int(x)


n, q = map(int, sys.stdin.readline().split())
a = [int(x) for x in sys.stdin.readline().split()]
aux = [int1(x) for x in sys.stdin.read().split()]

b = a[:]
for i in range(0, len(aux), 3):
    if aux[i] == 2: b.append(aux[i + 1])
    b.append(aux[i + 2])
b.sort()

c, m = {b[0]: 0}, 1
for i in range(1, len(b)):
    if b[i] != b[i - 1]:
        c[b[i]] = m
        m += 1


oracle = Ones(m)
for x in a:
    oracle.inc(c[x])

r = []
for i in range(0, len(aux), 3):
    if aux[i] == 1:
        index, salary = aux[i + 1] - 1, aux[i + 2]
        oracle.dec(c[a[index]])
        a[index] = salary
        oracle.inc(c[salary])
    else:
        r.append(str(oracle.count(c[aux[i + 1]], c[aux[i + 2]])))
sys.stdout.write('\n'.join(r))
