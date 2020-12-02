n = int(input()) - 1
p = 1 << n
M = p - 1
a = [0] * p

r = []
s, i = [0], ['0' * n]
while len(s) > 0:
    x = s[-1]
    if a[x] == 2:
        s.pop()
        r.append(i.pop())
    else:
        y = ((x << 1) | a[x]) & M
        s.append(y)
        i.append(a[x])
        a[x] += 1

print(*r, sep='')
