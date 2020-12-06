def read():
    global n, E, M, g, fromS, toL, SL
    n, m = map(int, input().split())
    E = n - 2
    M = (1 << E) - 1

    # read graph and find who points to the last city
    g, fromS, toL = [[0] * (n - 2) for _ in range(n - 2)], [], []
    SL = 0
    for _ in range(m):
        u, v = map(int, input().split())
        if u != 1 and v != 1 and u != n and v != n:
            g[u - 2][v - 2] += 1
        if u == 1 and v == n: SL += 1
        if u == 1 and v != 1 and v != n: fromS.append(v)
        if v == n and u != 1 and u != n: toL.append(u)


def pre():
    global o, no, z, nz, mask

    # log[32] = 5, log[63] = 5, log[64] = 6, log[127] = 6
    log = [0] * (1 << E)
    for i in range(E):
        log[1 << i] = i
        log[(1 << (i + 1)) - 1] = i

    # precalculate first one and first zero for each mask
    o, no = [0] * M, [0] * M
    z, nz = [0] * M, [0] * M
    for i in range(M):
        m = i ^ (i + 1)
        z[i], nz[i] = log[m], i | m
        m = i & -i
        o[i], no[i] = log[m], i ^ m

    # order masks by number of ones
    m, h = [0] * M, [0] * (E + 1)
    for i in range(1, M):
        m[i] = m[i & (i - 1)] + 1
        h[m[i]] += 1
    for i in range(1, E + 1):
        h[i] += h[i - 1]
    mask = [0] * (M - 1)
    for i in range(1, M):
        p = h[m[i]] - 1
        mask[p] = i
        h[m[i]] = p


def calc():
    if n == 2:
        print(SL)
        return

    P = 10**9 + 7

    d = [[0] * E for _ in range(M + 1)]
    for v in fromS:
        d[1 << (v - 2)][v - 2] += 1

    for m in mask:
        row = d[m]

        j = m
        while j != 0:
            v = o[j]
            j = no[j]
            while row[v] >= P:
                row[v] -= P
            if row[v] == 0: continue

            k = m
            while k != M:
                u = z[k]
                k = nz[k]
                if g[v][u]: d[m | (1 << u)][u] += row[v] * g[v][u]

    r = 0
    for v in toL:
        r += d[M][v - 2]
    print(r % P)


read()
pre()
calc()
