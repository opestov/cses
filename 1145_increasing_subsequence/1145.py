import bisect

n = int(input())
a = [int(x) for x in input().split()]

b = [0] * (n + 1)
m = 0
for x in a:
    i = bisect.bisect_left(b, x, 0, m)
    b[i] = x
    if i == m: m += 1
print(m)
