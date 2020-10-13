import sys


class Seg:
    def __init__(self, state):
        p2 = 1
        while p2 < len(state):
            p2 *= 2
        t = [0] * (2 * p2)
        for i in range(len(state)):
            t[p2 + i] = state[i]
        for i in range(p2 - 1, 0, -1):
            t[i] = t[2 * i] + t[2 * i + 1]
        self.p2 = p2
        self.t = t

    def sum(self, l, r):
        t, l, r, acc = self.t, l + self.p2, r + self.p2, 0
        while l <= r:
            if l % 2 == 1:
                acc += t[l]
                l += 1
            if r % 2 == 0:
                acc += t[r]
                r -= 1
            l, r = l // 2, r // 2
        return acc

    def set(self, i, x):
        t, i = self.t, i + self.p2
        t[i] = x
        i //= 2
        while i > 0:
            t[i] = t[2 * i] + t[2 * i + 1]
            i //= 2


n, q = map(int, sys.stdin.readline().split())
a = [int(x) for x in sys.stdin.readline().split()]
aux = [int(x) for x in sys.stdin.read().split()]

seg = Seg(a)
r = []
for i in range(0, len(aux), 3):
    k, a, b = aux[i], aux[i + 1], aux[i + 2]
    if k == 1: seg.set(a - 1, b)
    else: r.append(str(seg.sum(a - 1, b - 1)))
sys.stdout.write('\n'.join(r))
