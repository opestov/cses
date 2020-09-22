n = int(input())
a = [0] * (n + 1)
for i, x in enumerate(input().split()):
    a[i + 1] = int(x)

s = [0]
r = [0] * n
for i in range(1, n + 1):
    while a[s[-1]] >= a[i]:
        s.pop()
    r[i - 1] = s[-1]
    s.append(i)
print(*r)
