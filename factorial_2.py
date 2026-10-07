def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter the number to apply factorial to: "))

result = factorial(num)
print(result)