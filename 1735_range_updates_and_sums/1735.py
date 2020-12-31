class S():
    def __init__(self, a):
        p2 = 1
        while p2 < len(a):
            p2 = p2 * 2

        t = [0] * (p2 * 4 + 1)
        for i in range(len(a)):
            t[2 * (p2 + i)] = a[i]
        for i in range(p2 - 1, 0, -1):
            t[2 * i] = t[4 * i] + t[4 * i + 2]

        self.p2, self.t = p2, t

    def process(self, type, L, R, nx=0):
        t = self.t

        acc = 0
        s = [0, self.p2 - 1, 2]
        while len(s) > 0:
            v = s.pop()
            if v < 0:
                t[-v] = t[-2 * v] + t[-2 * v + 2]
                continue

            r, l = s.pop(), s.pop()
            if L > r or l > R: continue
            if L <= l and r <= R:
                if type == 1:
                    t[v] += nx * (r - l + 1)
                    t[v + 1] += nx
                elif type == 2:
                    t[v] = nx * (r - l + 1)
                    t[v + 1] = (1 << 30) | nx
                else:
                    acc += t[v]
                continue

            m = (l + r) // 2
            k1, k2 = 2 * v, 2 * v + 2
            if (1 << 30) & t[v + 1]:
                t[k1], t[k1 + 1] = t[v] // 2, (1 << 30) | t[v + 1]
                t[k2], t[k2 + 1] = t[k1], t[k1 + 1]
                t[v + 1] = 0
            elif t[v + 1] != 0:
                t[k1] += (m - l + 1) * t[v + 1]
                t[k1 + 1] += t[v + 1]
                t[k2] += (r - m) * t[v + 1]
                t[k2 + 1] += t[v + 1]
                t[v + 1] = 0

            if type != 3: s.append(-v)
            s.append(l), s.append(m), s.append(k1)
            s.append(m + 1), s.append(r), s.append(k2)
        if type == 3: return acc


import sys

sys.stdin.readline()
s = S([int(x) for x in sys.stdin.readline().split()])
q = [int(x) for x in sys.stdin.read().split()]

r = []
i = 0
while i < len(q):
    t, a, b = q[i], q[i + 1] - 1, q[i + 2] - 1
    if t != 3:
        s.process(t, a, b, q[i + 3])
        i += 1
    else:
        r.append(str(s.process(t, a, b)))
    i += 3

sys.stdout.write('\n'.join(r))
