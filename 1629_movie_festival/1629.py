import sys

d = [int(x) for x in sys.stdin.read().split()]
n = d[0]

perm = list(range(n))
perm.sort(key=lambda i: d[2 * i + 2])

k, t = 0, 0
for p in perm:
    a, b = d[2 * p + 1], d[2 * p + 2]
    if a >= t:
        k += 1
        t = b
print(k)
