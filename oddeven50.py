num = int(input("Enter a number: "))
if num >= 50:
    print("Above 50")
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")
else:
    print("Below 50")