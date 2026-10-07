def sum_down(n):
    if n == 0:
        return 0
    return n + sum_down(n - 1)

sum = int(input("Enter the number to sum down: "))

result = sum_down(sum)
print(result)