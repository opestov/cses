N = 10 ** 6 + 1
n = int(input())
p = [int(x) for x in input().split()]

s = list(range(N))
i = 2
while i * i < N:
    if s[i] == i:
        for j in range(i * i, N, i):
            if s[j] == j: s[j] = i
    i += 1

f, best = [False] * N, 1
for q in p:
    x, a = q, [1]
    d, exp, k = 0, 0, 0
    while x > 1:
        if s[x] != d: k, d, exp = len(a), s[x], 1
        exp *= d
        for i in range(k):
            z = a[i] * exp
            if f[z] and z > best: best = z
            f[z] = True
            a.append(z)
        x //= d
print(best)
