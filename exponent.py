base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
result = 1
while exponent > 0:
    if exponent % 2 == 1:
        result = result * base
    base = base * base
    exponent = exponent // 2

print("Answer: ", result)