import sys

n, m, q = map(int, sys.stdin.readline().split())
aux = [int(x) for x in sys.stdin.read().split()]

INF = 10**12
d = [INF] * (n * n)
for i in range(0, 3 * m, 3):
    a, b, c = aux[i:i + 3]
    p, q = n * (a - 1) + b - 1, n * (b - 1) + a - 1
    d[p], d[q] = min(d[p], c), min(d[q], c)
for i in range(0, n * n, n + 1):
    d[i] = 0

for k in range(n):
    for i in range(0, k):
        for j in range(i, k):
            d[i * n + j] = min(d[i * n + j], d[i * n + k] + d[j * n + k])
        for j in range(k, n):
            d[i * n + j] = min(d[i * n + j], d[i * n + k] + d[k * n + j])
    for i in range(k, n):
        for j in range(i, n):
            d[i * n + j] = min(d[i * n + j], d[k * n + i] + d[k * n + j])

r = []
for i in range(3 * m, len(aux), 2):
    a, b = aux[i:i + 2]
    z = min(d[(a - 1) * n + b - 1], d[(b - 1) * n + a - 1])
    r.append('-1' if z == INF else str(z))
sys.stdout.write('\n'.join(r))
