import collections

n = int(input())

q = collections.deque()
q.append(n)

d = [-1] * (n + 1)
d[n] = 0

while d[0] == -1 and len(q) > 0:
    x = q.popleft()
    y = x
    while y > 0:
        z = y % 10
        if d[x - z] == -1:
            d[x - z] = d[x] + 1
            q.append(x - z)
        y //= 10

print(d[0])
