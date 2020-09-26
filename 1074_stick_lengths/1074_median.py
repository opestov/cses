n = int(input())
a = [int(x) for x in input().split()]
a.sort()

k = n // 2

r = 0
for i in range(k):
    r += a[k] - a[i]
for i in range(k, n):
    r += a[i] - a[k]
print(r)
