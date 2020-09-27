import array, bisect

n = int(input())
a = [int(x) for x in input().split()]

t = array.array('i', [0] * n)
m = 0
for x in a:
    i = bisect.bisect_right(t, x, 0, m)
    if i == m: m += 1
    t[i] = x
print(m)
