import sys

M = 10**9 + 7

n = int(sys.stdin.readline())
q = [int(x) for x in sys.stdin.read().split()]

r = []
for i in range(0, len(q), 2):
    a, b = q[i], q[i + 1]
    r.append(str(pow(a, b, M)))
sys.stdout.write('\n'.join(r))
