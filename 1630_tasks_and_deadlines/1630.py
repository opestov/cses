import sys

aux = [int(x) for x in sys.stdin.read().split()]

n = aux[0]
p = list(range(n))
p.sort(key=lambda i: aux[2 * i + 1])

r, f = 0, 0
for i in range(n):
    a, d = aux[2 * p[i] + 1], aux[2 * p[i] + 2]
    f += a
    r += d - f
print(r)
