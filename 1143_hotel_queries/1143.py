class Hotels:
    def __init__(self, cap):
        p2 = 1
        while p2 < len(cap):
            p2 *= 2
        t = [0] * (2 * p2)
        for i in range(len(cap)):
            t[p2 + i] = cap[i]
        for i in range(p2 - 1, 0, -1):
            t[i] = max(t[2 * i], t[2 * i + 1])
        self.p2, self.t = p2, t

    def assign(self, x):
        t, p2 = self.t, self.p2
        if t[1] < x: return 0
        i = 1
        while i < p2:
            if t[2 * i] >= x: i = 2 * i
            else: i = 2 * i + 1
        hotel = i - p2 + 1

        t[i] = t[i] - x
        while i > 1:
            t[i // 2] = max(t[i], t[i ^ 1])
            i //= 2
        return hotel


import sys

n, m = map(int, sys.stdin.readline().split())
a = [int(x) for x in sys.stdin.readline().split()]
b = [int(x) for x in sys.stdin.readline().split()]

oracle = Hotels(a)
sys.stdout.write(' '.join([str(oracle.assign(x)) for x in b]))
