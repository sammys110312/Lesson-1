numbers = [4, 1, 2, 1, 2, 4, 7]

result = 0

for num in numbers:
    result = result ^ num

print("The number appearing once is", result)