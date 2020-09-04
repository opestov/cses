def find(r, c):
    m = max(r, c)
    x = (m - 1)**2
    if m % 2 == 0:
        if c == m:
            return x + r
        return x + m + m - c
    if r == m:
        return x + c
    return x + m + m - r


tests = int(input())
for t in range(tests):
    row, col = map(int, input().split())
    print(find(row, col))
