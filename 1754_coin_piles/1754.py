def one(a, b):
    if a > b: a, b = b, a
    if b - a > a: return False
    a -= b - a
    return a % 3 == 0


t = int(input())
for i in range(t):
    a, b = [int(x) for x in input().split()]
    print("YES" if one(a, b) else "NO")
