import sys

n = int(sys.stdin.readline())
a = [int(x) for x in sys.stdin.read().split()]

p = list(range(2 * n))
p.sort(key=lambda i: (a[i] << 1) + (i & 1))

k = 0
s = []
r = [0] * n
for x in p:
    if x & 1: s.append(r[x >> 1])
    elif len(s) > 0: r[x >> 1] = s.pop()
    else:
        k += 1
        r[x >> 1] = k
print(k)
print(*r)
