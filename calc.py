def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

x=int(input("Enter 1st Number Here: "))
y=int(input("Enter 2nd Number Here: "))
operation=(input("Enter What You Want To Do: "))

if operation == "+":
    print(addition(x,y))

elif operation == "-":
    print(subtraction(x,y))

elif operation == "*":
    print(multiply(x,y))

elif operation == "/":
    print(divide(x,y))

else:
    print("Invalid Operator")