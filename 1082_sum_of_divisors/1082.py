def f(n):
    r = 0

    i = 1
    while i * i <= n:
        r += i * (n // i)
        i += 1

    x = i
    j = 1
    while j * x <= n:
        y = n // j
        r += (x + y) * (y - x + 1) // 2
        j += 1

    return r


n = int(input())
print(f(n) % (10**9 + 7))
