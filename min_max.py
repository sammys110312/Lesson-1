def minElement(a, size):
    temp = a[0]
    for i in range(1, size):
        temp = min(temp, a[i])
    return temp
def maxElement(a, size):
    temp = a[0]
    for i in range(1, size):
        temp = max(temp, a[i])
    return temp
number = [10, 40, 20, 50, 30]
size = len(number)
minimum = minElement(number, size)
maximum = maxElement(number, size)
print(minimum)
print(maximum)