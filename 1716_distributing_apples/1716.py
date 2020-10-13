B = 10**9 + 7
n, m = map(int, input().split())

i, f, r = 1, 1, 1
while i <= m + n - 1:
    if i == n - 1: r = (r * pow(f, B - 2, B)) % B
    if i == m: r = (r * pow(f, B - 2, B)) % B
    if i == m + n - 1: r = (r * f) % B
    i = i + 1
    f = (f * i) % B
print(r)
