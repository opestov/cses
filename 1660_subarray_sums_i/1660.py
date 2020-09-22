n, s = map(int, input().split())
a = [int(x) for x in input().split()]

r = 0
p = 0
d = {0: 1}
for x in a:
    p += x
    if p - s in d:
        r += d[p - s]
    if p not in d:
        d[p] = 0
    d[p] += 1
print(r)
