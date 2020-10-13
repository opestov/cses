import sys

n, m = map(int, sys.stdin.readline().split())
a = [int(x) for x in sys.stdin.readline().split()]
q = [int(x) for x in sys.stdin.read().split()]
t = [0] * (n + 1)


def inc(i, delta):
    while i <= n:
        t[i] += delta
        i += (i & -i)


def s0(i):
    acc = 0
    while i > 0:
        acc += t[i]
        i = i & (i - 1)
    return acc


for i in range(n):
    inc(i + 1, a[i])

ans = []
for i in range(0, len(q), 3):
    x, y, z = q[i], q[i + 1], q[i + 2]
    if x == 1:
        delta = z - a[y - 1]
        a[y - 1] = z
        inc(y, delta)
    elif x == 2:
        ans.append(str(s0(z) - s0(y - 1)))
sys.stdout.write('\n'.join(ans))
