def binary_search(numbers,target):
    low = 0
    high = len(numbers) - 1

    while low <= high:
        middle = (low + high) // 2

        if numbers[middle] == target:
            return middle

        elif numbers[middle] < target:
            low = middle + 1

        else:
            high = middle - 1

    return -1

numbers = [1, 3, 4, 6, 9, 11, 12, 16]

number = binary_search(numbers, 11)
print(number)