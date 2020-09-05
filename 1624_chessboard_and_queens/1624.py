def tr(s):
    a = []
    for i, c in enumerate(s):
        if c == '.':
            a.append(i)
    return a


s = input()
n = len(s)
board = [tr(s)]
for i in range(1, n):
    board.append(tr(input()))

vert = [True] * n
plus = [True] * (2 * n - 1)
minus = [True] * (2 * n - 1)


def dfs(r):
    if r == n: return 1

    acc = 0
    for x in board[r]:
        if vert[x] and plus[x + r] and minus[x - r]:
            vert[x], plus[x + r], minus[x - r] = False, False, False
            acc += dfs(r + 1)
            vert[x], plus[x + r], minus[x - r] = True, True, True,
    return acc


print(dfs(0))
