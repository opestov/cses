import sys

E, M = 18, (1 << 18) - 1

n = int(sys.stdin.readline())
a = [int(x) for x in sys.stdin.read().split()]

events = []
for i in range(0, len(a), 3):
    events.append(((a[i] << 1) << E) | (i // 3))
    events.append((((a[i + 1] << 1) | 1) << E) | (i // 3))
events.sort()

s = [0] * n
c = 0
for e in events:
    i, t = e & M, (e >> E) & 1
    if t == 0: s[i] = c
    else: c = max(c, s[i] + a[3 * i + 2])
print(c)
