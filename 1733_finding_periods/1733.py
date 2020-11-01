s = input()
n = len(s)

p = [0] * n
for i in range(1, n):
    k = p[i - 1]
    while k > 0 and s[i] != s[k]:
        k = p[k - 1]
    p[i] = k + (s[i] == s[k])

i, r = p[n - 1], []
while i > 0:
    r.append(n - i)
    i = p[i - 1]
r.append(n)
print(*r)
