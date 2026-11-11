numbers = [1, 2, 3, 4, 5, 6, 7, 8]
k = 3
result = []
for i in range(0, len(numbers), k):
    group = numbers [i:i + k]
    reversed_group = group[::-1]
    result.extend(reversed_group)
print(numbers)
print(result)