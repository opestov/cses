import sys

N = 10**6
s, p, d = list(range(N + 1)), list(range(N + 1)), [1] * (N + 1)

i = 2
while i * i <= N:
    if s[i] == i:
        j, k = i * i, i
        while j <= N:
            if s[j] == j:
                s[j] = i
                if s[k] != i:
                    p[j], d[j] = i, 1
                else:
                    p[j], d[j] = i * p[k], 1 + d[k]
            j, k = j + i, k + 1
    i += 1

aux = [int(x) for x in sys.stdin.read().split()]
res = []
for i in range(1, len(aux)):
    x, y = aux[i], 1
    while x != 1:
        y *= d[x] + 1
        x //= p[x]
    res.append(str(y))
sys.stdout.write('\n'.join(res))


