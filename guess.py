import random

secret_number = random.randint(1, 10)

print("Guess the number between 1 and 10!")

while True:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Higher! Try again.")
    elif guess > secret_number:
        print("Lower! Try again.")
    else:
        print("Correct! You guessed the number.")
        break