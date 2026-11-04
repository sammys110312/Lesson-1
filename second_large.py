def second(arr):
    largest = None
    second_largest = None
    for num in arr:
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif num != largest and (second_largest is None or num > second_largest):
            second_largest = num
    if second_largest is None:
        return "Element does not exist"
    return second_largest
numbers = [10, 58, 30, 80, 20]
result = second(numbers)
print(result)