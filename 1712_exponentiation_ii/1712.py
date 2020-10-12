import sys

M = 10**9 + 7

n = int(sys.stdin.readline())
q = [int(x) for x in sys.stdin.read().split()]

r = []
for i in range(0, len(q), 3):
    a, b, c = q[i], q[i + 1], q[i + 2]
    r.append(str(pow(a, pow(b, c, M - 1), M)))
sys.stdout.write('\n'.join(r))
