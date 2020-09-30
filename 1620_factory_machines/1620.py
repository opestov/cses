n, t = map(int, input().split())
a = [int(x) for x in input().split()]

l, r = 0, t * a[0]
while l + 1 != r:
    m = (l + r) // 2
    k = 0
    for x in a:
        k += m // x
    if k >= t:
        r = m
    else:
        l = m

print(r)
