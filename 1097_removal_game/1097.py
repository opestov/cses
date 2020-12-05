n = int(input())
a = [int(x) for x in input().split()]

d, p = [a[:], [0] * n], 1
for l in range(2, n + 1):
    cc, m1 = d[p], d[1 - p]
    for i in range(0, n - l + 1):
        cc[i] = max(a[i] - m1[i + 1], a[i + l - 1] - m1[i])
    p = 1 - p
print((sum(a) + d[1 - p][0]) // 2)
