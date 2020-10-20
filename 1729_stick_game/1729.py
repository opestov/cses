n, k = map(int, input().split())
p = [int(x) for x in input().split()]

a = ['L'] * (n + 1)
for i in range(n + 1):
    if a[i] == 'L':
        for x in p:
            if i + x <= n: a[i + x] = 'W'
print(''.join(a[1:]))
