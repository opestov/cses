# Lyndon factorization

s = input()
n = len(s)

r = []

p, q, k = 0, 0, 1
for i in range(1, n):
    if s[i] == s[p + q]: q = 0 if q == k - 1 else q + 1
    elif s[i] > s[p + q]: q, k = 0, i - p + 1
    else:
        for j in range(p, i - q, k):
            r.append(s[j:j + k])
        p, q, k = i - q, 0, q + 1

for j in range(p, n, k):
    r.append(s[j:j + k])

print(r)
