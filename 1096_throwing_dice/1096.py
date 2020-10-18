M = 10**9 + 7
n = int(input())


def mm(a, b):
    c = [[0] * 6 for _ in range(6)]
    for i in range(6):
        for j in range(6):
            for k in range(6):
                c[i][j] += a[i][k] * b[k][j]
            c[i][j] = c[i][j] % M
    return c


p = [[0] * 6 for _ in range(5)]
for i in range(5):
    p[i][i + 1] = 1
p.append([1] * 6)

r = [[0] * 6 for _ in range(6)]
for i in range(6):
    r[i][i] = 1

while n > 0:
    if n % 2 == 1:
        r = mm(r, p)
    p = mm(p, p)
    n //= 2

s = [1]
for i in range(5):
    s.append(sum(s))

ans = 0
for i in range(6):
    ans += r[0][i] * s[i]
print(ans % M)
