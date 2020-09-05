def print_char(index, times):
    print(chr(index + ord('A')) * times, end='')


def main():
    s = input()

    h = [0] * 26
    for x in s:
        h[ord(x) - ord('A')] += 1

    m = -1
    for c in range(26):
        if h[c] % 2 == 1:
            if m != -1:
                print('NO SOLUTION')
                return
            m = c

    for c in range(26):
        if h[c] > 0 and c != m:
            print_char(c, h[c] // 2)
    if m != -1:
        print_char(m, h[m])
    for c in range(25, -1, -1):
        if h[c] > 0 and c != m:
            print_char(c, h[c] // 2)


main()
