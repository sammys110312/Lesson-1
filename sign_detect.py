a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
result = a ^ b
print("XOR result:", result)

if result < 0:
    print("Numbers have different signs")
else:
    print("Numbers have the same signs")