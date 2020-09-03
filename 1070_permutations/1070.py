class Solver:
    def __init__(self):
        self.n = int(input())

    def solve(self):
        if self.n == 1:
            print(1)
            return

        if self.n < 4:
            print('NO SOLUTION')
            return

        p = ' '.join(map(str, range(2, self.n+1, 2)))
        q = ' '.join(map(str, range(1, self.n+1, 2)))
        print(p, q)
    
s = Solver()
s.solve()

