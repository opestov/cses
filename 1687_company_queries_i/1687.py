import sys

n, q = map(int, sys.stdin.readline().split())
p = [0, 0]
for x in sys.stdin.readline().split():
    p.append(int(x))
a = [int(x) for x in sys.stdin.read().split()]

t = []
t.append(p)
for i in range(18):
    ti = t[-1]
    t.append([ti[ti[j]] for j in range(n + 1)])

r = []
for i in range(0, len(a), 2):
    x, k, j = a[i], a[i + 1], 0
    while x != 0 and k > 0:
        if k & 1: x = t[j][x]
        j, k = j + 1, k // 2
    r.append('-1' if x == 0 else str(x))
sys.stdout.write('\n'.join(r))
