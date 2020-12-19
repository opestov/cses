import sys

n, q = map(int, sys.stdin.readline().split())
a = sys.stdin.readlines()

s = [[0] * (n + 1) for _ in range(n + 1)]
t = [[0] * (n + 1) for _ in range(n + 1)]


def f(i, j):
    x = 1 - 2 * s[i][j]
    s[i][j] = 1 - s[i][j]

    r = i
    while r <= n:
        c = j
        while c <= n:
            t[r][c] += x
            c += -c & c
        r += -r & r


def q(i, j):
    acc, r = 0, i
    while r > 0:
        c = j
        while c > 0:
            acc += t[r][c]
            c &= c - 1
        r &= r - 1
    return acc


for i in range(n):
    for j in range(n):
        if a[i][j] == '*':
            f(i + 1, j + 1)
            s[i + 1][j + 1] = 1

r = []
for i in range(n, len(a)):
    b = [int(x) for x in a[i].split()]
    if b[0] == 1: f(b[1], b[2])
    else:
        y1, x1, y2, x2 = b[1:]
        z = q(y2, x2) - q(y2, x1 - 1) - q(y1 - 1, x2) + q(y1 - 1, x1 - 1)
        r.append(str(z))
sys.stdout.write('\n'.join(r))
