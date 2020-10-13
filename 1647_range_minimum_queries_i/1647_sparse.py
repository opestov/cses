import sys

n, m = map(int, sys.stdin.readline().split())
a = [[int(x) for x in sys.stdin.readline().split()]]
q = [int(x) for x in sys.stdin.read().split()]

i, k = 0, 1
while 2 * k <= n:
    b = []
    for j in range(n - 2 * k + 1):
        b.append(min(a[-1][j], a[-1][j + k]))
    a.append(b)
    i, k = i + 1, 2 * k

ans = []
for i in range(0, len(q), 2):
    le, ri = q[i] - 1, q[i + 1]
    e, p2 = 0, 1
    while 2 * p2 <= ri - le:
        e, p2 = e + 1, p2 * 2
    ans.append(str(min(a[e][le], a[e][ri - p2])))
sys.stdout.write('\n'.join(ans))
