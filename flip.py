def flip_number(n, reversed_num = 0):
    if n == 0:
        return reversed_num
    last_digit = n % 10
    reversed_num = reversed_num * 10 + last_digit
    return flip_number(n // 10, reversed_num)

number = int(input("Enter a number: "))
if number == 0:
    result = 0
else:
    result = flip_number(abs(number))
    if number < 0:
        result = - result
print(result)