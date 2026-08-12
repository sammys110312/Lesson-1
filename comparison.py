import math

size = [10, 100, 1000]

for n in size:
    constant = 1
    log = math.log2(n)
    linear = n
    quadratic = n**2
    print(n)
    print(constant)
    print(round(log, 2))
    print(linear)
    print(quadratic)