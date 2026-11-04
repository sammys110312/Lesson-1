def find_mean(arr):
    total = 0
    for num in arr:
        total = total + num
    size = len(arr)
    mean = total/size
    return mean
def find_median(arr):
    arr.sort()
    size = len(arr)
    if size % 2 != 0:
        middle = size // 2
        return arr[middle]
    else:
        middle1 = size // 2 - 1
        middle2 = size // 2
        median = (arr[middle1]+ arr[middle2]) / 2
        return median
number = [10, 40, 20, 50, 30]
mean_result = find_mean(number)
median_result = find_median(number)
print(mean_result)
print(median_result)