n, x = map(int, input().split())
p = [int(x) for x in input().split()]

p.sort()

r = 0
i, j = 0, n - 1
while i < j:
    if p[i] + p[j] <= x:
        i += 1
    j -= 1
    r += 1
if i == j:
    r += 1
print(r)
