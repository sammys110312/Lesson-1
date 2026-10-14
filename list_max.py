def list_max(numbers):
    if numbers == []:
        raise ValueError("List cannot be empty.")
    if len(numbers) == 1:
        return numbers[0]
    head = numbers[0]
    tail = numbers[1:]
    max_tail = list_max(tail)
    if head > max_tail:
        return head
    else: 
        return max_tail
numbers = [5, 13, 24, 51, 31, 28, 2, 1331, 1428]
result = list_max(numbers)
print(numbers)
print(result)