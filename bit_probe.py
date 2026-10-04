n = int(input("Enter a number: "))
j = int(input("Enter a bit position to check: "))
bit = (n >> j) & 1
if bit == 1:
    print("Bit", j, "is ON")
else:
    print("Bit", j, "is OFF")
    