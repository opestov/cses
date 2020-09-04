class Solver:
    def __init__(self):
        _ = input()
        a = [int(x) for x in input().split()]

        s = 0
        for i in range(1, len(a)):
            if a[i] < a[i - 1]:
                s += a[i - 1] - a[i]
                a[i] = a[i - 1]
        self.ans = s


s = Solver()
print(s.ans)
