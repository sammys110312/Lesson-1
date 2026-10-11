def bounce(n):
    if n == 0:
        return
    bounce(n - 1)
    print(n)
number = 5
bounce(number)