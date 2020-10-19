import sys

t = int(sys.stdin.readline())
a = [int(x) for x in sys.stdin.read().split()]

r = []
i = 0
for _ in range(t):
    x = 0
    for j in range(a[i]):
        x ^= a[i + j + 1]
    r.append(str('first' if x else 'second'))
    i += a[i] + 1

sys.stdout.write('\n'.join(r))
