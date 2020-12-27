s = input()
n = len(s)
s += s

r = 0
p, q, k = 0, 0, 1
for i in range(1, 2 * n):
    if s[i] == s[p + q]:
        q = 0 if q == k - 1 else q + 1
    elif s[i] > s[p + q]:
        q, k = 0, i - p + 1
    else:
        if p < n: r = p
        p, q, k = i - q, 0, q + 1

print(s[p:p + n])
