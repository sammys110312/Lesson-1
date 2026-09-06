def hcf(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // hcf(a, b)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("LCM =", lcm(x, y))