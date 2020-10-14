import sys

n, q = map(int, sys.stdin.readline().split())
aux = [int(x) for x in sys.stdin.read().split()]

p = [0] * (n + 1)
for i in range(1, n + 1):
    p[i] = p[i - 1] ^ aux[i - 1]

r = []
for i in range(n, len(aux), 2):
    a, b = aux[i], aux[i + 1]
    r.append(str(p[b] ^ p[a - 1]))
sys.stdout.write('\n'.join(r))
