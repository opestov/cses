import bisect

x, n = map(int, input().split())
a = [int(x) for x in input().split()]

p = a[:]
p.append(0)
p.append(x)
p.sort()

seg = [0] * (n + 1)
for i in range(n + 1):
    seg[i] = p[i + 1] - p[i]
left, right = list(range(n + 1)), list(range(n + 1))

res = [0] * n
m = max(seg)
for i in range(n - 1, -1, -1):
    res[i] = m
    j = bisect.bisect_left(p, a[i])

    x, y = left[j - 1], right[j]
    seg[x] = seg[x] + seg[j]
    right[x], left[y] = y, x
    m = max(m, seg[x])

print(*res)
