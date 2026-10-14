def list_sum(numbers):
    if numbers == []:
        return 0
    head = numbers[0]
    tail = numbers[1:]
    return head + list_sum(tail)
numbers = [10, 20, 30, 40, 50, 60, 70 ,80, 90, 100]
result =  list_sum(numbers)
print(numbers)
print(result)