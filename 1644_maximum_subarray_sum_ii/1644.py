n, a, b = map(int, input().split())
d = [int(x) for x in input().split()]
k = b - a + 1

s = [0] * (n + 1)
for i, x in enumerate(d):
    s[i + 1] = s[i] + x

p = [0] * (n + 1)
for i in range(0, n + 1, k):
    p[i] = s[i]
    for j in range(i + 1, min(i + k, n + 1)):
        p[j] = min(p[j - 1], s[j])

q = [0] * (n + 1)
for i in range(0, n + 1, k):
    z = min(i + k - 1, n)
    q[z] = s[z]
    for j in range(z - 1, i - 1, -1):
        q[j] = min(q[j + 1], s[j])


def mmm(j):
    if j < k - 1: return p[j]
    i = j + 1 - k
    return min(q[i], p[j])


r = -2 * (10**14)
for i in range(a, n + 1):
    r = max(r, s[i] - mmm(i - a))
print(r)
