numbers = [1, 1, 0, 1, 1, 1, 0, 1]
count = 0
maximum = 0
for i in range (len(numbers)):
    if numbers[i] == 1:
        count += 1
    else:
        count = 0
    if count > maximum:
        maximum = count
print(maximum)