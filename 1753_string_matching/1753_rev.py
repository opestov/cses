t = input()

s = input()
n = len(s)
p = [0] * n


def pp(c, k):
    while k > 0 and c != s[n - k - 1]:
        k = p[n - k]
    return k + (c == s[n - k - 1])


for i in range(n - 2, -1, -1):
    p[i] = pp(s[i], p[i + 1])

r, k = 0, 0
for i in range(len(t) - 1, -1, -1):
    k = pp(t[i], k)
    if k == n: r, k = r + 1, p[0]
print(r)
