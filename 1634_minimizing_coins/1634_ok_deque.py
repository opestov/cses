import collections

n, s = map(int, input().split())
c = [int(x) for x in input().split()]

d = [-1] * (s + 1)
q = collections.deque()
q.append(0)
d[0] = 0

while d[s] == -1 and len(q) > 0:
    x = q.popleft()
    for y in c:
        if x + y <= s and d[x + y] == -1:
            d[x + y] = d[x] + 1
            q.append(x + y)

print(d[s])
