k = int(input())

z = [[] for i in range(64)]
for r in range(8):
    for c in range(8):
        if r > 0: z[r * 8 + c].append((r - 1) * 8 + c)
        if r < 7: z[r * 8 + c].append((r + 1) * 8 + c)
        if c > 0: z[r * 8 + c].append(r * 8 + c - 1)
        if c < 7: z[r * 8 + c].append(r * 8 + c + 1)

m = [[0] * 64 for _ in range(2)]
a = [1] * 64


def go(r, c):
    for j in range(64):
        m[0][j] = 0
    m[0][8 * r + c] = 1

    p = 0
    for i in range(k):
        cc, nn = m[p], m[1 - p]
        for j in range(64):
            nn[j] = 0
        for j in range(64):
            for n in z[j]:
                nn[n] += cc[j] / len(z[j])
        p = 1 - p

    for j in range(64):
        a[j] *= (1 - m[p][j])


for r in range(8):
    for c in range(8):
        go(r, c)
print("{:.6f}".format(sum(a)))
