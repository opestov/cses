B = 10**9 + 7

n = int(input())

s = ((n + 1) * n) // 2
if s % 2 == 1:
    print(0)
    exit()
s //= 2

d = [0] * (s + 1)
d[0] = 1
for i in range(1, n):
    for j in range(s, i - 1, -1):
        d[j] = (d[j] + d[j - i]) % B
print(d[s])
