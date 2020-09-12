n = int(input())
a = [int(x) for x in input().split()]
a.sort()

k = sum(a) - n * a[0]
r = k
for i in range(1, n):
    x = a[i] - a[i - 1]
    k += i * x
    k -= (n - i) * x
    r = min(r, k)
print(r)
