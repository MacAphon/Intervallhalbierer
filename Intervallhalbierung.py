import math

def zeros(self, f, a, b, steps):
    """calculates an approximate zero. f, a, b, steps"""
    if steps == 0:
        return [a, b]

    resultA = f(a)
    resultB = f(b)
    middle = (a + b)/2
    resultM = f(middle)
    steps -= 1

    if resultA == 0:
        return [a, a]
    elif resultB == 0:
        return [b, b]
    elif resultM == 0:
        return [middle, middle]

    if (resultA > 0) != (resultM > 0):
        return zeros(f, a, middle, steps)
    else:
        return zeros(f, middle, b, steps)

print(zeros(lambda x: -(x**2) + 2, -4, 0, 10))
print(zeros(lambda x: math.sin(x), 1, 4, 10))
