def main():
    n = int(input())
    p = [int(x) for x in input().split()]

    s = sum(p)
    best = s

    mask = [0] * n
    gray = list(range(n - 1))

    cur = 0
    while len(gray) > 0:
        i = gray.pop()
        gray += range(i + 1, n - 1)

        if mask[i] == 0:
            cur += p[i]
        else:
            cur -= p[i]
        mask[i] = 1 - mask[i]

        best = min(best, abs(s - cur - cur))

    print(best)


main()
