_ = int(input())
a = [int(x) for x in input().split()]

m = max(a)
f = [0] * (m + 1)
for x in a:
    f[x] += 1

for i in range(m, 0, -1):
    c = 0
    for j in range(i, m + 1, i):
        c += f[j]
        if c > 1: break
    if c > 1:
        print(i)
        break
