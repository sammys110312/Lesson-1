def iterative_binary_search(seats, target):
    low = 0
    high = len(seats) - 1

    while low <= high:
        mid = (low + high) // 2

        if seats[mid] == target:
            return mid
        elif seats[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def recursive_binary_search(seats, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if seats[mid] == target:
        return mid
    elif seats[mid] < target:
        return recursive_binary_search(seats, target, mid + 1, high)
    else:
        return recursive_binary_search(seats, target, low, mid - 1)


seats = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41]

target = int(input("Enter a train seat number to find: "))

iterative_result = iterative_binary_search(seats, target)

recursive_result = recursive_binary_search(
    seats, target, 0, len(seats) - 1
)

if iterative_result != -1:
    print("Iterative search: Seat found at index", iterative_result)
else:
    print("Iterative search: Seat not found")

if recursive_result != -1:
    print("Recursive search: Seat found at index", recursive_result)
else:
    print("Recursive search: Seat not found")