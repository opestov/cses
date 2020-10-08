"""
Tried three different ways to compress coordinates:
1) Dict 0.19
2) Manual pairs x << E | y 0.14
3) Python tuples 0.68
"""


class Seg:
    def __init__(self, domain):
        self.p2 = 1
        while self.p2 < domain:
            self.p2 *= 2
        self.t = [0] * (2 * self.p2)

    def change(self, i, delta):
        i += self.p2
        while i > 0:
            self.t[i] += delta
            i //= 2

    def inc(self, i):
        self.change(i, 1)

    def dec(self, i):
        self.change(i, -1)

    def kth(self, k):
        i, l, r, z = 1, 0, self.p2, k
        while l + 1 != r:
            m = (l + r) // 2
            if self.t[2 * i] >= z:
                i, r = 2 * i, m
            else:
                i, l, z = 2 * i + 1, m, z - self.t[2 * i]
        return l


def main():
    n, k = map(int, input().split())
    a = [int(x) for x in input().split()]

    EXP, MASK = 18, (1 << 18) - 1
    b = [a[i] << EXP | i for i in range(n)]
    b.sort()

    m = -1
    c = [0] * n
    d = [0] * n
    for i in range(n):
        if i == 0 or b[i] >> EXP != b[i - 1] >> EXP:
            m += 1
            d[m] = b[i] >> EXP
        c[b[i] & MASK] = m
    m += 1

    seg = Seg(m)
    kth = (k + 1) // 2
    for i in range(k - 1):
        seg.inc(c[i])

    res = []
    for i in range(k - 1, n):
        seg.inc(c[i])
        med = seg.kth(kth)
        res.append(d[med])
        seg.dec(c[i - k + 1])
    print(*res)


main()
