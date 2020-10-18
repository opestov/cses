M = 10**9 + 7
n = int(input())

f, g = 1, 1
a, b = 0, 1
while n > 0:
    if n % 2 == 1:
        a, b = ((g - f) * a + f * b) % M, (f * a + g * b) % M
    f, g = (2 * f * g - f * f) % M, (f * f + g * g) % M
    n //= 2

print(a)
