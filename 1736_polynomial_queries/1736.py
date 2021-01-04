def f(i, x):
    j = i
    while j <= n:
        z = j - i
        t2[j] += x
        t1[j] += (2 * z + 1) * x
        t0[j] += (z * z + z) * x
        j += -j & j


def s(i):
    acc, j = 0, i
    while j > 0:
        k = i - j + 1
        acc += t2[j] * k * k + t1[j] * k + t0[j]
        j &= j - 1
    return acc // 2


import sys

n, _ = map(int, sys.stdin.readline().split())
v = [int(x) for x in sys.stdin.readline().split()]
q = [int(x) for x in sys.stdin.read().split()]

t0, t1, t2 = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
f(1, v[0])
f(2, v[1] - 2 * v[0])
for i in range(2, n):
    f(i + 1, v[i] - 2 * v[i - 1] + v[i - 2])

r = []
for i in range(0, len(q), 3):
    t, a, b = q[i:i + 3]
    if t == 1:
        f(a, 1)
        f(b + 1, a - b - 2)
        f(b + 2, b - a + 1)
    else:
        r.append(str(s(b) - s(a - 1)))
sys.stdout.write('\n'.join(r))
