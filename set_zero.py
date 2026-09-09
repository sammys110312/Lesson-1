number = 40
position = 1

mask = 1 << position

number = number | mask
print(number)

number = 42
position = 1
mask = ~(1 << position)
number = number & mask
print(number)