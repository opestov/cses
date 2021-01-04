# Segment tree where nodes are sorted lists. Intresting implementation using
# list `mem` as memory for all lists. Unfortunately TL in Python.
#
# It works correctly without sorting at the beginning but sorting improves
# performance (I expect that we have less cache misses).


class T():
    def __init__(self, a):
        N = 4000000
        mem = [0] * N

        d = {}
        n = len(a)
        for i in range(len(a) - 1, -1, -1):
            x = a[i]
            a[i] = d.get(x, n)
            d[x] = i

        p2 = 1
        while p2 < n:
            p2 *= 2
        h = [0] * (2 * p2)
        for i in range(n):
            h[p2 + n - i - 1] = i
            mem[i] = a[n - i - 1]
        for i in range(p2 - 1, 0, -1):
            h[i] = n
            p, q = h[2 * i], h[2 * i + 1]
            P, Q = h[2 * i - 1], h[2 * i]
            while p < P or q < Q:
                if q == Q or (p < P and mem[p] <= mem[q]):
                    mem[n] = mem[p]
                    n, p = n + 1, p + 1
                else:
                    mem[n] = mem[q]
                    n, q = n + 1, q + 1
        h[0] = n
        self.p2, self.mem, self.h = p2, mem, h

    def q(self, l, r):
        mem, h, x = self.mem, self.h, r + 1
        l, r = self.p2 + l, self.p2 + r

        acc = 0
        while l <= r:
            if l & 1:
                i, j = h[l], h[l - 1]
                acc += j - i if mem[i] >= x else j - bisect_left(mem, x, i, j)
                l += 1
            if (r & 1) == 0:
                i, j = h[r], h[r - 1]
                acc += j - i if mem[i] >= x else j - bisect_left(mem, x, i, j)
                r -= 1
            l //= 2
            r //= 2
        return acc


import sys
from bisect import bisect_left

n, q = map(int, sys.stdin.readline().split())
t = T([int(x) for x in sys.stdin.readline().split()])

q1 = [int(x) - 1 for x in sys.stdin.read().split()]
o, h = [0] * q, [0] * (n + 1)
for i in range(0, 2 * q, 2):
    h[q1[i]] += 1
for i in range(1, n + 1):
    h[i] += h[i - 1]
for i in range(0, 2 * q, 2):
    p = h[q1[i]] - 1
    o[p] = i // 2
    h[q1[i]] = p

r = [None] * q
for i in o:
    r[i] = str(t.q(q1[2 * i], q1[2 * i + 1]))

sys.stdout.write('\n'.join(r))
