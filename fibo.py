def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    first = fibonacci(n - 1)
    second = fibonacci(n - 2)
    return first + second

number = 10
result = fibonacci(number)
print("Fibonacci number:", result)
