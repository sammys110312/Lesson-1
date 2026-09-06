num = int(input("Enter a number: "))
if num & 1:
    print(num, "is odd")
else:
    print(num, "is even")
count = 0
temp = num
while temp > 0:
    if temp & 1:
        count += 1
    temp = temp >> 1
print("Number of 1s", count)
print("Binary:", bin(num))