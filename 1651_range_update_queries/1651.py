class Seg:
    def __init__(self, a):
        p2 = 1
        while p2 < len(a):
            p2 *= 2
        t = [0] * (2 * p2)
        t[p2] = a[0]
        for i in range(1, len(a)):
            t[p2 + i] = a[i] - a[i - 1]
        for i in range(p2 - 1, 0, -1):
            t[i] = t[2 * i] + t[2 * i + 1]
        self.t, self.p2 = t, p2

    def __add(self, i, d):
        t = self.t
        i += self.p2
        while i > 0:
            t[i] += d
            i //= 2

    def inc(self, i, j, k):
        self.__add(i - 1, k)
        if j < self.p2: self.__add(j, -k)

    def item(self, i):
        t, i, acc = self.t, self.p2 + i - 1, 0
        while i & -i != i:
            if i % 2 == 0: acc += t[i]
            i = (i - 1) // 2
        return acc + t[i]


import sys

n, m = map(int, sys.stdin.readline().split())
a = [int(x) for x in sys.stdin.readline().split()]
aux = [int(x) for x in sys.stdin.read().split()]

seg = Seg(a)
ans = []
i = 0
while i < len(aux):
    if aux[i] == 1:
        seg.inc(aux[i + 1], aux[i + 2], aux[i + 3])
        i += 4
    else:
        ans.append(str(seg.item(aux[i + 1])))
        i += 2
sys.stdout.write('\n'.join(ans))
