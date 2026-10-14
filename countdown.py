def countdown(number):
    if number == 0:
        print("Time is up!")
        return

    print(number)
    countdown(number - 1)

countdown(5)

def build_and_unwind(level):
    if level == 0:
        print("Base case reached. Now unwinding begins.")
        return

    print("Building level:", level)
    build_and_unwind(level - 1)
    print("Unwinding level:", level)

build_and_unwind(3)

def count_up(number):
    if number > 10:
        return

    print(number)
    count_up(number + 1)

count_up(1)

def factorial(number):
    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)

print("5! =", factorial(5))

def unsafe_countdown(number):
    print(number)