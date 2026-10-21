def circle_prob(n):
    safe = 1
    powof2 = 1
    index = 1
    while (n > powof2):
        print("Before loop -", n, safe, index, powof2)
        safe = (n - powof2) * 2+1
        index = index + 1
        powof2 = pow(2, index)
        print("After loop -",n, safe, index, powof2)
    return safe



people = int(input("How many people are in the circle? "))
guess = int(input("Which position do you think is safe? "))

answer = circle_prob(people)

if guess == answer:
    print("Correct! You chose the safe position.")
else:
    print(f"Wrong! The safe position is {answer}.")