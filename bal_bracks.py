def count_brackets(n, opened = 0, closed = 0):
    if opened == n and closed == n:
        return 1
    ways = 0
    if opened < n:
        ways += count_brackets(n, opened + 1, closed)
    if closed < opened:
        ways += count_brackets(n, opened, closed + 1)
    return ways

pairs = int(input("Enter the number of pairs: "))
total = count_brackets(pairs)
print("Number of balanced sequences:", total)