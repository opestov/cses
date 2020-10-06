import sys

B = 10**9 + 7

n = int(sys.stdin.readline())
g = sys.stdin.read().split()

d = [[0] * (n + 1), [0] * (n + 1)]
d[0][0] = 1
r = 1
for i in range(n):
    for j in range(n):
        if g[i][j] == '.':
            d[r][j] = (d[r][j - 1] + d[1 - r][j]) % B
        else:
            d[r][j] = 0
    r = 1 - r

print(d[1 - r][n - 1])
