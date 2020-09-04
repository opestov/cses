n = int(input())
s = (n + 1) * n // 2

if s % 2 == 1:
    print('NO')
else:
    l, r = 0, n
    while l + 1 < r:
        k = (l + r) // 2
        if (n + n - k + 1) * k < s:
            l = k
        else:
            r = k

    pivot = s // 2 - (n + n - l + 1) * l // 2

    print('YES')
    print(l + 1)
    print(pivot, ' '.join(map(str, range(n, n - l, -1))))
    print(n - l - 1)
    if pivot == 1:
        print(' '.join(map(str, range(n - l, pivot, -1))))
    else:
        print(' '.join(map(str, range(1, pivot))),
              ' '.join(map(str, range(n - l, pivot, -1))))
