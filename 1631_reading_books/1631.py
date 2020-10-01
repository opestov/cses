n = int(input())
a = [int(x) for x in input().split()]

s = sum(a)
m = max(a)
if 2 * m >= s:
    print(2 * m)
else:
    print(s)
