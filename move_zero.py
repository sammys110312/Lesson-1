numbers = [0, 1, 0, 3, 12]
n = len(numbers)
write = 0
for i in range(n):
    if numbers[i] != 0:
        numbers[write] = numbers[i]
        write = write + 1
while write < n:
    numbers[write] = 0
    write = write + 1
print("List after moving zeros:", numbers)