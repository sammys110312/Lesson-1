def name_flip(s):
    if s == "":
        return ""
    return name_flip(s[1:]) + s[0]
name = input("Enter your name: ")
reversed_name = name_flip(name)
print(reversed_name)