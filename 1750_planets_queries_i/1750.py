import sys

n, q = map(int, input().split())
t = [int(x) - 1 for x in input().split()]
a = [int(x) for x in sys.stdin.read().split()]

d = [t]
for i in range(1, 31):
    d.append([t[t[j]] for j in range(n)])
    t = d[-1]

r = []
for i in range(0, len(a), 2):
    x, k, i = a[i] - 1, a[i + 1], 0
    while k > 0:
        if k & 1: x = d[i][x]
        k = k >> 1
        i += 1
    r.append(str(x + 1))
sys.stdout.write('\n'.join(r))
