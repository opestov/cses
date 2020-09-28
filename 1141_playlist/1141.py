n = int(input())
a = [int(x) for x in input().split()]

s = set()
r, j = 0, 0
for i in range(n):
    if a[i] in s:
        while True:
            s.remove(a[j])
            j += 1
            if a[j - 1] == a[i]: break
    r = max(r, i - j + 1)
    s.add(a[i])

print(r)
