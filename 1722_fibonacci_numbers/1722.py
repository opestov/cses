B = 10**9 + 7
n = int(input())


def mul(m1, m2):
    a1, b1, c1, d1 = m1
    a2, b2, c2, d2 = m2
    a3 = (a1 * a2 + b1 * c2) % B
    b3 = (a1 * b2 + b1 * d2) % B
    c3 = (c1 * a2 + d1 * c2) % B
    d3 = (c1 * b2 + d1 * d2) % B
    return a3, b3, c3, d3


p = 0, 1, 1, 1
r = 1, 0, 0, 1
while n > 0:
    if n % 2 == 1:
        r = mul(r, p)
    p = mul(p, p)
    n //= 2

print(r[1])
