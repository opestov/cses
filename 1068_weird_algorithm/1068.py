def next(x):
    if x % 2 == 0:
        return x // 2
    return 3 * x + 1


n = int(input())
a = [n]
while a[-1] != 1:
    a.append(next(a[-1]))

print(*a)
