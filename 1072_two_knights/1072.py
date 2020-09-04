def calc(n):
    if n < 4: return [0, 0, 6, 28][n]

    total = n * n * (n * n - 1) // 2
    good = (n - 2) * ((n - 4) * 4 + 10) + (n - 4) * 2 + 4
    return total - good


m = int(input())
for i in range(1, m + 1):
    print(calc(i))
