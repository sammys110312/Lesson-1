num_chars = int(input("How many characters would you like to preview? "))

file = open("class-notes.txt","r")
content = file.read()
print(content)
file.close()

file = open("class-notes.txt","r")
lines = file.readlines()
for i in range(len(lines)):
    print(i+1, "-", lines[i].strip())
file.close()

skip = input("Enter subject to skip: ")
file = open("class-notes.txt","r")
for line in file:
    if skip in line:
        print("skip:", line.strip)
    else:
        print("keep:", line.strip)
file.close()

file = open("class-notes.txt","r")
new_file = open("cleaned-notes.txt", "w")
line_num = 1
for line in lines:
    if line_num % 2 !=0:
        new_file.write(line)
    line_num = line_num + 1
new_file.close()
file.close()
print("Odd line copied")