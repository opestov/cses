import sys

t = int(sys.stdin.readline())
a = [int(x) for x in sys.stdin.read().split()]

i = 0
r = []
while i < len(a):
    n = a[i]
    i += 1
    x = 0
    for j in range(i + 1, i + n, 2):
        x = x ^ a[j]
    r.append('second' if x == 0 else 'first')
    i += n

sys.stdout.write('\n'.join(r))
