class List:
    def __init__(self, a):
        p2 = 1
        while p2 < len(a):
            p2 *= 2
        t = [0] * (2 * p2)
        for i in range(len(a)):
            t[p2 + i] = 1
        for i in range(p2 - 1, 0, -1):
            t[i] = t[2 * i] + t[2 * i + 1]
        self.p2, self.t, self.a = p2, t, a

    def remove(self, k):
        p2, t = self.p2, self.t
        i = 1
        while i < p2:
            if t[2 * i] >= k: i = 2 * i
            else: i, k = 2 * i + 1, k - t[2 * i]
        x = a[i - p2]
        while i > 0:
            t[i] -= 1
            i //= 2
        return x


import sys

n = int(sys.stdin.readline())
a = [int(x) for x in sys.stdin.readline().split()]
b = [int(x) for x in sys.stdin.readline().split()]

oracle = List(a)
sys.stdout.write(' '.join(str(oracle.remove(x)) for x in b))
