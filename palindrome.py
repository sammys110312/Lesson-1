number = int(input("Enter a number: "))
original_num = number
rev = 0
while number > 0:
    digit = number % 10
    rev = rev * 10 + digit
    number = number // 10
if original_num == rev:
    print("It is a palindrome")
else:
    print("It is not a palindrome")