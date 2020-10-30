s = input()
n = len(s)

p = [0] * n
for i in range(1, n):
    k = p[i - 1]
    while k > 0 and s[i] != s[k]:
        k = p[k - 1]
    p[i] = k + 1 if s[i] == s[k] else k

i, r = p[n - 1], []
while i > 0:
    r.append(i)
    i = p[i - 1]
r.reverse()
print(*r)
