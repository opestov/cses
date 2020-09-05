def next(a):
    n = len(a)

    i = n - 1
    while i > 0 and a[i - 1] >= a[i]:
        i -= 1
    if i == 0: return False

    i -= 1
    j = n - 1
    while a[j] <= a[i]:
        j -= 1
    a[i], a[j] = a[j], a[i]
    a[i + 1:] = a[:i:-1]

    return True


s = sorted(map(ord, input()))
a = []
a.append(bytes(s).decode())
while next(s):
    a.append(bytes(s).decode())

print(len(a))
print(*a, sep='\n')
