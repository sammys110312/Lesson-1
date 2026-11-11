numbers = [10, 20, 30, 40, 50]
k = 2
n = len(numbers)
if n == 0:
    rotated = []
else:
    k = k % n
    first = numbers[k:]
    second = numbers[:k]
    rotated = first + second
print(numbers)
print(rotated)