n = int(input())
r = [int(x) for x in input().split()]

acc = 0.0
for i in range(n):
    for j in range(i + 1, n):
        x = (r[i] - 1) / (2 * r[j])
        y = 1 - (r[j] + 1) / (2 * r[i])
        acc += x if r[i] <= r[j] else y
print("{:.6f}".format(acc))
