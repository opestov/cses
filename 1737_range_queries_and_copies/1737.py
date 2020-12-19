class T():
    def __init__(self, a):
        N = 2000000
        n = 1
        while n < len(a):
            n *= 2
        for _ in range(n - len(a)):
            a.append(0)

        t, x, z, l, r = [0] * N, [0] * N, [0] * N, [0] * N, [0] * N
        for i in range(n, n * 2):
            t[i], x[i], z[i] = a[i - n], i - n, 1
        for i in range(n - 1, 0, -1):
            t[i], x[i], z[i] = t[2 * i] + t[2 * i + 1], x[2 * i], 2 * z[2 * i]
            l[i], r[i] = 2 * i, 2 * i + 1
        self.n, self.t, self.x, self.z, self.l, self.r = n * 2, t, x, z, l, r

    def sum(self, v, xx, zz):
        t, x, z, l, r = self.t, self.x, self.z, self.l, self.r
        acc = 0
        s = [v]
        while len(s) > 0:
            u = s.pop()
            if x[u] + z[u] <= xx or xx + zz <= x[u]: continue
            if xx <= x[u] and xx + zz >= x[u] + z[u]:
                acc += t[u]
                continue
            s.append(l[u])
            s.append(r[u])
        return acc

    def update(self, v, i, val):
        n, t, x, z, l, r = self.n, self.t, self.x, self.z, self.l, self.r
        s = [v]
        while z[v] > 1:
            if i * 2 < x[v] * 2 + z[v]: s.append(l[v])
            else: s.append(r[v])
            v = s[-1]

        t[n], x[n], z[n] = val, x[v], 1
        n += 1
        for i in range(len(s) - 2, -1, -1):
            u = s[i]
            if l[u] == s[i + 1]: ll, rr = n - 1, r[u]
            else: ll, rr = l[u], n - 1
            t[n], x[n], z[n], l[n], r[n] = t[ll] + t[rr], x[ll], z[u], ll, rr
            n += 1
        self.n = n
        return n - 1


import sys


def main():
    sys.stdin.readline()
    t = T([int(x) for x in sys.stdin.readline().split()])
    q = [int(x) for x in sys.stdin.read().split()]

    arrays = [1]

    r = []
    i = 0
    while i < len(q):
        x, k = q[i], q[i + 1] - 1
        if x == 1:
            arrays[k] = t.update(arrays[k], q[i + 2] - 1, q[i + 3])
            i += 4
        elif x == 2:
            r.append(
                str(t.sum(arrays[k], q[i + 2] - 1, q[i + 3] - q[i + 2] + 1)))
            i += 4
        else:
            arrays.append(arrays[k])
            i += 2
    sys.stdout.write('\n'.join(r))


main()
