import sys

n, m = map(int, sys.stdin.readline().split())
aux = [int(x) for x in sys.stdin.read().split()]

d = [0] * (n + 1)
p = [-1] * (n + 1)


def bw(v):
    c = []
    while v != -1:
        c.append(v)
        z = v
        v, p[z] = p[v], -1
    c.reverse()
    return c[:c.index(c[0], 1) + 1]


def fb():
    for i in range(n - 1):
        for j in range(0, len(aux), 3):
            a, b, c = aux[j], aux[j + 1], aux[j + 2]
            if d[a] + c < d[b]:
                p[b] = a
                d[b] = d[a] + c

    for j in range(0, len(aux), 3):
        a, b, c = aux[j], aux[j + 1], aux[j + 2]
        if d[b] > d[a] + c:
            print('YES')
            print(*bw(b))
            exit()
    print('NO')

fb()
