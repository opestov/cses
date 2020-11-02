t = input()

s = input()
n = len(s)
p = [0] * n


def pp(c, k):
    while k > 0 and c != s[k]:
        k = p[k - 1]
    return k + (c == s[k])


for i in range(1, n):
    p[i] = pp(s[i], p[i - 1])

r, k = 0, 0
for c in t:
    k = pp(c, k)
    if k == n: r, k = r + 1, p[k - 1]
print(r)
