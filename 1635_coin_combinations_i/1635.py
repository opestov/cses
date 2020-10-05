n, s = map(int, input().split())
a = [int(x) for x in input().split()]
a.sort()

d = [0] * (s + 1)
d[0] = 1
for i in range(0, s + 1):
    if d[i] != 0:
        for x in a:
            if i + x > s: break
            d[i + x] = (d[i + x] + d[i]) % (10**9 + 7)
print(d[s])
