m = ["LURD?".index(c) for c in input()]
if m.count(4) == 48:
    print(88418)
    exit()
if [x // 4 for x in m].index(0) >= 24:
    m.reverse()
    for i in range(48):
        if m[i] == 0 or m[i] == 2: m[i] = 2 - m[i]

d = (-1, -8, 1, 8)
f = [0] * 64
for i in range(7, 64, 8):
    f[i] = 1
for i in range(56, 64):
    f[i] = 1

k = 0

s = [0 if m[0] == 4 else m[0]]
f[0], i = 1, 1
while i > 0:
    p, z = s[-1] >> 3, s[-1] & 7
    if z == 4:
        s.pop()
        i -= 1
        f[p] = 0
        continue
    s[-1] += 1 if m[i - 1] == 4 else 4 - z

    p1 = p + d[z]
    if f[p1]: continue
    if p1 == 48:
        if i == 48: k += 1
        continue

    p2 = p1 + d[z]
    mr = d[(z + 1) & 3]
    if f[p2] or f[p2 - mr] or f[p2 + mr]:
        if not (f[p - mr] and f[p1 - mr] and f[p2 - mr]):
            if not (f[p + mr] and f[p1 + mr] and f[p2 + mr]):
                continue

    s.append((p1 << 3) | (0 if m[i] == 4 else m[i]))
    f[p1] = 1
    i += 1

print(k)
