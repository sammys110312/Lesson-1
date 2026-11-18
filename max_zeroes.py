numbers = [0, 0, 1, 0, 0, 0, 1, 0]
count = 0
maximum = 0
for i in range (len(numbers)):
    if numbers[i] == 0:
        count += 1
    else:
        count = 0
    if count > maximum:
        maximum = count
print(maximum)