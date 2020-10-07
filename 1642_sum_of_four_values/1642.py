n, s = map(int, input().split())
a = [int(x) for x in input().split()]

p = {}
for j in range(n):
    for i in range(j):
        p[a[i] + a[j]] = max((i, j), p.get(a[i] + a[j], (0, 0)))

for j1 in range(n):
    for i1 in range(j1):
        i2, j2 = p.get(s - a[i1] - a[j1], (0, 0))
        if i2 > j1:
            print(i1 + 1, j1 + 1, i2 + 1, j2 + 1)
            exit()

print('IMPOSSIBLE')
