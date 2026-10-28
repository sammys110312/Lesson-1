keys = {
    "2":"ABC",
    "3":"DEF",
    "4":"GHI",
    "5":"JKL",
    "6":"MNO",
    "7":"PQRS",
    "8":"TUV",
    "9":"WXYZ"
}
def count_combos(digits):
    if digits == "":
        return 1
    first_digit = digits[0]
    choices = len(keys[first_digit])
    remaining_digits = digits[1:]
    remaining_combos = count_combos(remaining_digits)
    return choices * remaining_combos
digits = input("Enter digits from 2 - 9: ")
if all(digit in keys for digit in digits) and digits != "":
    result = count_combos(digits)
    print(result)
else: 
    print("Enter more digits from 2 to 9")