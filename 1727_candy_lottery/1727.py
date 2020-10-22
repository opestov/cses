n, k = map(int, input().split())
print("{:.6f}".format(k - sum(i**n for i in range(k)) / (k**n)))
