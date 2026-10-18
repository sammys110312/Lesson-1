def power_four(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    return power_four(n // 4)
number = int(input("Enter number: "))
result = power_four(number)
if result:
    print("This number is a power of 4")
else:
    print("This number is not a power of 4")