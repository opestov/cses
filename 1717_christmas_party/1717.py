M = 10 ** 9 + 7
n = int(input())

p, q = 1, 0
for i in range(2, n + 1):
    p, q = q, (i - 1) * (p + q) % M
print(q)
