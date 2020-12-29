class S():
    def __init__(self, a):
        n = len(a)
        p2 = 1
        while p2 < n:
            p2 *= 2

        ss, extra = [0] * p2, [0] * p2
        mi, ma = [0] * 2 * p2, [0] * 2 * p2

        mi[p2], ma[p2] = 0, 0
        for i in range(p2 + 1, 2 * p2):
            x = a[i - p2] if i < n + p2 else 0
            mi[i] = mi[i - 1] + x
            ma[i] = mi[i]
        for i in range(p2 - 1, 0, -1):
            mi[i] = min(mi[2 * i], mi[2 * i + 1])
            ma[i] = max(ma[2 * i], ma[2 * i + 1])
            ss[i] = ma[2 * i + 1] - mi[2 * i]
            if 2 * i < p2: ss[i] = max(ss[i], ss[2 * i], ss[2 * i + 1])

        self.a, self.p2 = a, p2
        self.ss, self.mi, self.ma, self.extra = ss, mi, ma, extra

    def q(self):
        return max(0, self.ss[1])

    def update(self, i, x):
        d = x - self.a[i]
        self.a[i] = x
        p2, ss, mi, ma, extra = self.p2, self.ss, self.mi, self.ma, self.extra

        l, r = i + p2, 2 * p2 - 1
        while l < r:
            if (l & 1):
                mi[l], ma[l] = mi[l] + d, ma[l] + d
                if l < p2: extra[l] += d
                l += 1
            l, r = l // 2, r // 2
        mi[l], ma[l], extra[l] = mi[l] + d, ma[l] + d, extra[l] + d

        i = (i + p2) // 2
        while i > 0:
            mi[i] = min(mi[2 * i], mi[2 * i + 1]) + extra[i]
            ma[i] = max(ma[2 * i], ma[2 * i + 1]) + extra[i]
            ss[i] = ma[2 * i + 1] - mi[2 * i]
            if 2 * i < p2: ss[i] = max(ss[i], ss[2 * i], ss[2 * i + 1])
            i = i // 2


import sys

sys.stdin.readline()
a = [0]
for x in sys.stdin.readline().split():
    a.append(int(x))
s = S(a)

q = [int(x) for x in sys.stdin.read().split()]
r = []
for i in range(0, len(q), 2):
    s.update(q[i], q[i + 1])
    r.append(str(s.q()))

sys.stdout.write('\n'.join(r))
