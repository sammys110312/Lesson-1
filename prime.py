num = int(input("Enter a number: "))
prime = True
for i in range(2,num):
    if num % i == 0:
        prime = False
        break
if prime and num > 1:
    print("Prime Number")
else:
    print("Not A Prime Number")