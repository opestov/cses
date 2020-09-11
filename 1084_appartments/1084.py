n, m, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

a.sort()
b.sort()

r, j = 0, 0
for i in range(n):
    while j < m and a[i] - k > b[j]:
        j += 1
    if j < m and b[j] >= a[i] - k and b[j] <= a[i] + k:
        r += 1
        j += 1
print(r)
