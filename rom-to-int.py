values = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}

roman = input("Enter a number in Roman form: ")

total = 0

for i in range(len(roman)):
    current_value = values[roman[i]]
    if i + 1 < len(roman):
        next_value = values[roman[i+1]]
        if current_value < next_value:
            total = total - current_value
        else:
            total = total + current_value
    else:
        total = total + current_value

print(total)