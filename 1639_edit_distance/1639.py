s = input()
t = input()

if len(s) > len(t): s, t = t, s
n, m = len(s), len(t)

d = [list(range(m + 1)), [0] * (m + 1)]
p = 1
for i in range(1, n + 1):
    cc, m1 = d[p], d[1 - p]
    cc[0] = i
    for j in range(1, m + 1):
        if s[i - 1] == t[j - 1]:
            cc[j] = m1[j - 1]
        else:
            cc[j] = min(m1[j], m1[j - 1], cc[j - 1]) + 1
    p = 1 - p
print(d[1 - p][m])
