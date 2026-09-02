from math import sqrt
number = int(input("Enter your number: "))
if number < 2:
    print("Not a prime")
else:
    yes_prime = True
    for i in range(2, int(sqrt(number) + 1)):
        if number % i == 0:
            yes_prime = False
        break
    if yes_prime:
        print("It is a prime")
    else:
        print("Not a prime")