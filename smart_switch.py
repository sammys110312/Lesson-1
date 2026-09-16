switch_value = 173

def show_bits(n):
    return format(n, "08b")

binary_value = show_bits(switch_value)

ones = binary_value.count("1")
zeros = binary_value.count("0")

print("=== Smart Switches ===")
print("Switch Value:", switch_value)
print("Binary:", binary_value)
print("ON switches:", ones)
print("OFF switches:", zeros)

temp = switch_value
count = 0

while temp > 0:
    if temp & 1:
        count += 1
    temp = temp >> 1

print("\nSet bits using while loop:", count)

temp = switch_value
position = 0

while temp & 1 == 0:
    temp = temp >> 1
    position += 1

print("First ON switch position:", position)

print("\n=== Bit Masks ===")

for i in range(8):
    mask = 1 << i
    print("Position", i, "Mask:", mask, "Binary:", show_bits(mask))

switch_names = [
    "Living Room",
    "Kitchen",
    "Bedroom",
    "Bathroom",
    "Garage",
    "Garden",
    "Front Door",
    "Alarm"
]

print("\n=== Switch Status ===")

for i in range(8):
    mask = 1 << i

    if switch_value & mask:
        status = "ON"
    else:
        status = "OFF"

    print(switch_names[i], ":", status)

print("\n=== Final Summary ===")
print("Switch Value:", switch_value)
print("Binary:", show_bits(switch_value))
print("Total ON switches:", ones)
print("Total OFF switches:", zeros)
print("First ON switch position:", position)