a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print("Before swapping: ")
print("A -", a)
print("B -", b)
a = a ^ b
b = a ^ b
a = a ^ b
print("After swapping: ")
print("A -", a)
print("B -", b)