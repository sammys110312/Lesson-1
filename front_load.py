numbers = [3, 5, 4, -2]
current_sum = 0
max_sum = numbers[0]
for num in numbers:
    current_sum = current_sum + num
    if current_sum > max_sum:
        max_sum = current_sum
    if current_sum < 0:
        current_sum = 0
print(max_sum)