print("=== Two-Digit Prime Numbers ===")

for number in range(10, 100):
    prime = True

    for divisor in range(2, number):
        if number % divisor == 0:
            prime = False
            break

    if prime:
        print(number, end=" ")

print()