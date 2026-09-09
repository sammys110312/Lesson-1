number = 22
position = 2

mask = 1 << position
if number & mask:
    print("Bit is ON")
else:
    print("Bit is OFF")

