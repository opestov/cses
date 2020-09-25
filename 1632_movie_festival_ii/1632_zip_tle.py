import random, sys


class Node:
    def __init__(self, x):
        y = 0
        while random.randint(0, 1) == 0:
            y += 1

        self.key = x
        self.rank = y
        self.q = 1
        self.left = None
        self.right = None


def zip_add(v, x):
    if v is None: return Node(x)
    if x == v.key:
        v.q += 1
        return v
    if x < v.key:
        aux = zip_add(v.left, x)
        if aux.key == x:
            if aux.rank >= v.rank:
                v.left = aux.right
                aux.right = v
                return aux
            v.left = aux
    else:
        aux = zip_add(v.right, x)
        if aux.key == x:
            if aux.rank > v.rank:
                v.right = aux.left
                aux.left = v
                return aux
            v.right = aux
    return v


def zip_zip(a, b):
    if a is None: return b
    if b is None: return a
    if b.rank > a.rank:
        b.left = zip_zip(a, b.left)
        return b
    a.right = zip_zip(a.right, b)
    return a


def zip_remove(v, x):
    if v is None: return None
    if x == v.key:
        if v.q > 1:
            v.q -= 1
            return v
        return zip_zip(v.left, v.right)
    if x < v.key: v.left = zip_remove(v.left, x)
    else: v.right = zip_remove(v.right, x)
    return v


def zip_maxleq(v, x, cur):
    if v is None: return cur
    if x == v.key: return x
    if x < v.key: return zip_maxleq(v.left, x, cur)
    return zip_maxleq(v.right, x, v.key)


aux = [int(x) for x in sys.stdin.read().split()]
n, k = aux[0], aux[1]

p = list(range(n))
p.sort(key=lambda i: aux[2 * i + 3])

root = None
for i in range(k):
    root = zip_add(root, 0)

r = 0
for i in p:
    a, b = aux[2 * i + 2], aux[2 * i + 3]
    z = zip_maxleq(root, a, None)
    if z is None:
        continue

    root = zip_remove(root, z)
    root = zip_add(root, b)
    r += 1

print(r)
