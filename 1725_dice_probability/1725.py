F = 6
n, a, b = map(int, input().split())

d = [0.0] * (6 * n + 1 + F)
d[0 + F] = 1.0
for i in range(1, n + 1):
    for j in range(6 * i + F, i - 1 + F, -1):
        d[j] = sum(d[j - 6:j]) / 6
    for j in range(i + F):
        d[j] = 0

print("{:.6f}".format(sum(d[a + F:b + 1 + F])))
