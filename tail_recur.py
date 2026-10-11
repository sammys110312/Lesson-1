def tail_sum(n, total = 0):
    if n == 0:
        return total
    total = total + n
    return tail_sum(n - 1, total)
number = 5
result = tail_sum(number)
print("Sum =", number)