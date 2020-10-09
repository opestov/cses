import collections, sys

n, m = map(int, sys.stdin.readline().split())
g = sys.stdin.read().split()
d = [0] * ((n + 1) * (m + 1))
e = [-1] * ((n + 1) * (m + 1))


def init():
    global start
    q = collections.deque()

    for r in range(n):
        for c in range(m):
            i = r * (m + 1) + c
            if g[r][c] != '#': d[i] = -1
            if g[r][c] == 'A': start = i
            if g[r][c] == 'M':
                q.append(i)
                d[i] = 0

    while len(q) > 0:
        i = q.popleft()
        for j in [i - 1, i + 1, i - m - 1, i + m + 1]:
            if d[j] == -1:
                q.append(j)
                d[j] = d[i] + 1


def path(i):
    p = []
    while i != start:
        r, c = i // (m + 1), i % (m + 1)
        if r > 0 and e[i - m - 1] + 1 == e[i]:
            p.append('D')
            i -= m + 1
        elif r < n - 1 and e[i + m + 1] + 1 == e[i]:
            p.append('U')
            i += m + 1
        elif c > 0 and e[i - 1] + 1 == e[i]:
            p.append('R')
            i -= 1
        elif c < m - 1 and e[i + 1] + 1 == e[i]:
            p.append('L')
            i += 1
    p.reverse()
    return p


def main():
    init()

    q = collections.deque()
    q.append(start)
    e[start] = 0
    while len(q) > 0:
        i = q.popleft()
        r, c = i // (m + 1), i % (m + 1)
        if r == 0 or r == n - 1 or c == 0 or c == m - 1:
            return path(i)
        for j in [i - 1, i + 1, i - m - 1, i + m + 1]:
            if (d[j] == -1 or d[j] > e[i] + 1) and e[j] == -1:
                q.append(j)
                e[j] = e[i] + 1


ans = main()
if ans is None:
    print("NO")
else:
    print("YES")
    print(len(ans))
    print(''.join(ans))
