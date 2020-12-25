s = input()
n = len(s)

a, p = [1] * n, 0
x, y = 1, 1
for i in range(1, n):
    if y >= i:
        j = x + y - i
        if i + a[j] - 1 < y:
            a[i] = a[j]
            continue
        x = 2 * i - y
    else:
        x, y = i, i
    while x > 0 and y < n - 1 and s[x - 1] == s[y + 1]:
        x, y = x - 1, y + 1
    a[i] = y - i + 1
    if a[i] > a[p]: p = i

b, q = [0] * n, 0
x, y = 0, 0
for i in range(1, n):
    if y >= i:
        j = x + y - i
        if i + b[j] < y:
            b[i] = b[j]
            continue
        x = 2 * i - y
    else:
        x, y = i, i
    while x > 0 and y < n and s[x - 1] == s[y]:
        x, y = x - 1, y + 1
    b[i] = y - i
    if b[i] > b[q]: q = i

if 2 * a[p] - 1 > 2 * b[q]:
    print(s[p - a[p] + 1:p + a[p]])
else:
    print(s[q - b[q]:q + b[q]])
