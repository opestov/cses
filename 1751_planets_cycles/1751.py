n = int(input())
t = [int(x) - 1 for x in input().split()]

c, d, o = [-1] * n, [0] * n, []
for i in range(n):
    if c[i] != -1: continue

    s = [i]
    c[i], x = i, t[i]
    while c[x] == -1:
        s.append(x)
        c[x], x = i, t[x]

    if c[x] == i:
        z = len(o)
        for y in s:
            c[y] = z
        j = s.index(x)
        for k in range(j):
            d[s[k]] = j - k
        o.append(len(s) - j)
    else:
        for k in range(len(s)):
            c[s[k]] = c[x]
            d[s[k]] = d[x] + len(s) - k

for i in range(n):
    d[i] = d[i] + o[c[i]]
print(*d)
