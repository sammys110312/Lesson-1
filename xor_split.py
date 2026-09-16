numbers = [1, 2, 3, 2, 1, 5, 5, 7]

xor_all = 0

for num in numbers:
    xor_all = xor_all ^ num

right_bit = xor_all & xor_all

group1 = 0
group2 = 0

for num in numbers:
    if num & right_bit:
        group1 = group1 ^ num
    else:
        group2 = group2 ^ num
print("Odd occuring numbers are:", group1 , group2)