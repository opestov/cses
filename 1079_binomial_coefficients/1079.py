class Cnk:
    def __init__(self, n=10**6, m=10**9 + 7):
        f, g = [1] * (n + 1), [1] * (n + 1)
        for i in range(2, n + 1):
            f[i] = (f[i - 1] * i) % m
        g[n] = pow(f[n], m - 2, m)
        for i in range(n - 1, 0, -1):
            g[i] = (g[i + 1] * (i + 1)) % m
        self.m, self.f, self.g = m, f, g

    def calc(self, n, k):
        return (self.f[n] * self.g[k] * self.g[n - k]) % self.m


import sys

n = int(sys.stdin.readline())
aux = [int(x) for x in sys.stdin.read().split()]

oracle = Cnk()
r = []
for i in range(0, len(aux), 2):
    r.append(str(oracle.calc(aux[i], aux[i + 1])))
sys.stdout.write('\n'.join(r))
