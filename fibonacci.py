def fibonacci(n):
    if n < 0:
        return "Incorrect input"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Get input from user
n = int(input("Enter the position of the seqence: "))
print(fibonacci(n))