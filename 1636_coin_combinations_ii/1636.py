n, s = map(int, input().split())
a = [int(x) for x in input().split()]

d = [0] * (s + 1)
d[0] = 1
for x in a:
    for i in range(0, s - x + 1):
        d[i + x] = (d[i + x] + d[i]) % (10**9 + 7)
print(d[s])
