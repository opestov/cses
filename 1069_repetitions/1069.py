s = input() + '$'
a = 1
c, k = s[0], 1
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        k += 1
    else:
        a = max(a, k)
        c, k = s[i], 1
print(a)
