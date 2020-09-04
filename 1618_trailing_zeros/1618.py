def calc(n, x):
    acc = 0
    y = x
    while y <= n:
        acc += n // y
        y *= x
    return acc


n = int(input())
print(calc(n, 5))
