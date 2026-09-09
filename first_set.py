number = 40
position = 0
while number % 2 == 0:
    number = number >> 1
    position = position + 1

print(position)