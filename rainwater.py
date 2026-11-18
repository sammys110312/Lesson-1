height = [3, 0, 2, 0, 4]
n = len(height)
total_water = 0
for i in range(n):
    left_max = height[i]
    right_max = height[i]
    for j in range(i + 1):
        if height[j] > left_max:
            left_max = height[j]
    for j in range(i, n):
        if height[j] > right_max:
            right_max = height[j]
    water_level = min(left_max, right_max)
    trapped = water_level - height[i]
    total_water = total_water + trapped
print(total_water)