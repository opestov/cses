import sys
n, m = map(int, sys.stdin.readline().split())

s = [[0] * (n + 1) for _ in range(n + 1)]
for r in range(n):
    row = sys.stdin.readline()
    for c in range(n):
        if row[c] == '*': s[r + 1][c + 1] += 1
for r in range(1, n + 1):
    for c in range(1, n + 1):
        s[r][c] += s[r - 1][c] + s[r][c - 1] - s[r - 1][c - 1]

q = [int(x) for x in sys.stdin.read().split()]
a = []
for i in range(0, len(q), 4):
    r1, c1, r2, c2 = q[i:i + 4]
    x = s[r2][c2] - s[r1 - 1][c2] - s[r2][c1 - 1] + s[r1 - 1][c1 - 1]
    a.append(str(x))
sys.stdout.write('\n'.join(a))
