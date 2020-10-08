class Seg:
    def __init__(self, domain):
        self.p2 = 1
        while self.p2 < len(domain):
            self.p2 *= 2
        self.d = domain
        self.t1 = [0] * (2 * self.p2)
        self.t2 = [0] * (2 * self.p2)

    def change(self, i, d1, d2):
        i += self.p2
        while i > 0:
            self.t1[i] += d1
            self.t2[i] += d2
            i //= 2

    def add(self, i):
        self.change(i, 1, self.d[i])

    def remove(self, i):
        self.change(i, -1, -self.d[i])

    def cntsum_less(self, k):
        i, l, r, z = 1, 0, self.p2, k
        acc, sum = 0, 0
        while l + 1 != r:
            m = (l + r) // 2
            if self.t1[2 * i] >= z:
                i, r = 2 * i, m
            else:
                acc, sum = acc + self.t1[2 * i], sum + self.t2[2 * i]
                i, l, z = 2 * i + 1, m, z - self.t1[2 * i]
        return self.d[l], acc, sum


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

    seg = Seg(d[:m])
    mid = (k + 1) // 2
    for i in range(k - 1):
        seg.add(c[i])

    res = []
    for i in range(k - 1, n):
        seg.add(c[i])
        med, acc, p = seg.cntsum_less(mid)
        q = seg.t2[1] - p
        res.append(med * acc - p + q - med * (k - acc))
        seg.remove(c[i - k + 1])
    print(*res)


main()
