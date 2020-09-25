n, k = map(int, input().split())
a = [int(x) for x in input().split()]

l, r = 0, sum(a)
while l + 1 != r:
    m = (l + r) // 2

    s, acc = 0, 0
    for x in a:
        if x > m:
            acc = k + 1
            break
        if x > s:
            acc += 1
            if acc > k: break
            s = m
        s -= x
    if acc <= k:
        r = m
    else:
        l = m

print(r)
