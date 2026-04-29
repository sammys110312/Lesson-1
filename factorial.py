def factorial(num):
    if num == 1:
        return 1
    return num*factorial(num-1)
    
num1=int(input("Enter Number Here: "))
print(factorial(num1))