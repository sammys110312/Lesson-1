a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
xor_result = a ^ b
count = 0
while xor_result > 0:
    if xor_result & 1:
        count += 1
    xor_result = xor_result >> 1
print("Number of differnet bits", count)