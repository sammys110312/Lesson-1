n = int(input("Enter a number: "))
if n > 0:
    if (n & (n-1)) == 0:
        position = n.bit_length() - 1
        if position % 2 == 0:
            print(n, "is a power of 4")
        else:
            print(n, "is not a power of 4")
    else:
        print(n, "is not a power of 4")
else:
    print(n, "is not a power of 4")

if n > 0:
    if (n & (n-1)) == 0:
        position = n.bit_length() - 1
        if position % 3 == 0:
            print(n, "is a power of 8")
        else:
            print(n, "is not a power of 8")
    else:
        print(n, "is not a power of 8")
else:
    print(n, "is not a power of 8")