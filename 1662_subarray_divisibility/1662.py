n = int(input())
a = [int(x) for x in input().split()]

r = 0
p = 0
d = {0: 1}
for x in a:
    p = (p + x) % n
    if p not in d:
        d[p] = 0
    r += d[p]
    d[p] += 1
print(r)
