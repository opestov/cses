n = int(input())
s = sum(int(x) for x in input().split())
print(n*(n + 1) // 2 - s)
