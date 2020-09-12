n, s = map(int, input().split())
a = [int(x) for x in input().split()]

b = a[:]
b.sort()

i, j = 0, n - 1
p, q = None, None
while i < j:
    while i < j and b[i] + b[j] > s:
        j -= 1
    if i < j and b[i] + b[j] == s:
        p, q = b[i], b[j]
        break
    i += 1

if p is None:
    print('IMPOSSIBLE')
else:
    i = a.index(p)
    j = a.index(q) if p != q else a.index(p, i + 1)
    print(i + 1, j + 1)
