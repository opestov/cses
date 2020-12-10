import sys

n, q = map(int, sys.stdin.readline().split())
p = [0, 0]
for x in sys.stdin.readline().split():
    p.append(int(x))
a = [int(x) for x in sys.stdin.read().split()]

dest, h = [0] * (n - 1), [0] * (n + 2)
for i in range(2, n + 1):
    h[p[i]] += 1
for i in range(1, len(h)):
    h[i] += h[i - 1]
for i in range(2, n + 1):
    u = p[i]
    dest[h[u] - 1] = i
    h[u] -= 1

s, loc = [1], [h[1]]
cc, fc, tc = 1, [0] * (n + 1), [0] * (n + 1)
fc[1] = 1
while len(s) > 0:
    v, z = s[-1], loc[-1]
    if z == h[v + 1]:
        s.pop(), loc.pop()
        cc += 1
        tc[v] = cc
        continue
    u, loc[-1] = dest[z], z + 1
    cc += 1
    fc[u] = cc
    s.append(u), loc.append(h[u])
fc[0], tc[0] = 0, cc + 1

t = []
t.append(p)
for i in range(18):
    ti = t[-1]
    t.append([ti[ti[j]] for j in range(n + 1)])

r = []
for i in range(0, len(a), 2):
    x, y, k = a[i], a[i + 1], 17
    if fc[x] <= fc[y] and tc[y] <= tc[x]:
        r.append(str(x))
        continue
    while k >= 0:
        z = t[k][x]
        if not (fc[z] <= fc[y] and tc[y] <= tc[z]):
            x = z
        k = k - 1
    r.append(str(t[0][x]))

sys.stdout.write('\n'.join(r))
