def head_tail(numbers):
    if numbers == []:
        print("Empty List: Stopping program")
        return
    head = numbers[0]
    tail = numbers[1:]
    print("Head:", head)
    print("Tail:", tail)
    head_tail(tail)
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
head_tail(numbers)