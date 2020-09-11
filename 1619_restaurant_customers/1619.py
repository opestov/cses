import sys

aux = list(map(int, sys.stdin.read().split()))
e = [0] * (len(aux) - 1)
t = 0
for i, x in enumerate(aux):
    if i == 0: continue
    e[i - 1] = (x << 1) + t
    t = 1 - t

e.sort()
res, k = 0, 0
for x in e:
    k += 1 - 2 * (x & 1)
    res = max(res, k)
print(res)
