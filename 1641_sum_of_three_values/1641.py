n, s = map(int, input().split())
a = [int(x) for x in input().split()]

b = [(a[i], i + 1) for i in range(n)]
b.sort()
for i in range(n):
    a[i] = b[i][0]


def f():
    for j in range(1, n - 1):
        if a[0] + a[j] + a[j + 1] > s: continue
        if a[j - 1] + a[j] + a[-1] < s: continue
        i = 0
        for k in range(n - 1, j, -1):
            if a[j - 1] + a[j] + a[k] < s: break
            while i < j and a[i] + a[j] + a[k] < s:
                i += 1
            if i < j and a[i] + a[j] + a[k] == s:
                return b[i][1], b[j][1], b[k][1]


res = f()
if res is None: print('IMPOSSIBLE')
else: print(*res)
