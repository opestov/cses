n, m, g = 8, 10, [-21, -19, -12, -8, 8, 12, 19, 21]
a = [0 if r < n and c < n else -1 for r in range(m) for c in range(m)]
b = [8 + sum(a[i + x] for x in g) if a[i] == 0 else 0 for i in range(m * m)]


def moves(i):
    return [y for _, y in sorted((-b[i + x], i + x) for x in g if not a[i + x])]


x, y = map(int, input().split())
start = (y - 1) * m + x - 1
a[start] = 1
for delta in g:
    b[start + delta] -= 1
s, loc = [start], [moves(start)]
while True:
    if len(s) == n * n:
        for i in range(n):
            print(*a[i * m:i * m + n])
        exit()

    p = s[-1]
    if len(loc[-1]) == 0:
        s.pop(), loc.pop()
        a[p] = 0
        for delta in g:
            b[p + delta] += 1
        continue

    q = loc[-1].pop()
    a[q] = a[p] + 1
    for delta in g:
        b[q + delta] -= 1
    s.append(q)
    loc.append(moves(q))
