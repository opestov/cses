n = int(input())
a = [int(x) for x in input().split()]

s, m, r = 0, 0, a[0]
for x in a:
    s += x
    r = max(r, s - m)
    m = min(m, s)
print(r)
