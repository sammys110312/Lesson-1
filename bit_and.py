num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
bin1 = bin(num1)
bin2 = bin(num2)
print("Binary of", num1, ":", bin1)
print("Binary of", num2, ":", bin2)

and_result = num1 & num2
print("AND result:", and_result)
or_result = num1 | num2
print("OR result:", or_result)