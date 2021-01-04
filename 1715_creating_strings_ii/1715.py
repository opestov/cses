M = 10**9 + 7

s = [ord(c) - ord('a') for c in input()]
q = [0] * 26
for c in s:
    q[c] += 1

f = [1] * (1 + len(s))
for i in range(2, len(f)):
    f[i] = (f[i - 1] * i) % M

r = f[len(s)]
for x in q:
    if x != 0: r = (r * pow(f[x], M - 2, M)) % M
print(r)
