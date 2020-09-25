import bisect, sys

n, k = map(int, sys.stdin.readline().split())
a = [int(x) for x in sys.stdin.read().split()]

aux = a[:]
aux.sort()
m = 0
for i in range(1, 2 * n):
    if aux[m] != aux[i]:
        m += 1
        aux[m] = aux[i]
m += 1
for i in range(2 * n):
    a[i] = bisect.bisect_left(aux, a[i], 0, m)

p = list(range(n))
p.sort(key=lambda i: a[2 * i + 1])

m2 = 1
while m2 < m:
    m2 *= 2

sum = [0] * (2 * m2)
rig = [-1] * (2 * m2)
j = m2
while j > 0:
    sum[j], rig[j], j = k, 0, j // 2

ans = 0
for i in p:
    x, y = a[2 * i], a[2 * i + 1]
    if sum[x + m2] > 0:
        pos = x
    else:
        v, l, r, pos = 1, 0, m2, -1
        while l + 1 < r:
            c = (l + r + 1) // 2
            if x < c:
                v, r = 2 * v, c
            else:
                v, l, pos = 2 * v + 1, c, max(pos, rig[2 * v])

    if pos != -1:
        j = m2 + pos
        if sum[j] == 1: rig[j] = -1
        while j > 0:
            sum[j] -= 1
            if j < m2: rig[j] = max(rig[2 * j], rig[2 * j + 1])
            j = j // 2
        j = m2 + y
        while j > 0:
            sum[j] += 1
            rig[j] = max(rig[j], y)
            j = j // 2

        ans += 1

print(ans)
