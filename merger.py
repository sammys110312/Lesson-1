import os

with open("science.txt","r") as f:
    science = f.read()
    print(science)

with open("maths.txt","r") as f:
    for line in f:
        words = line.split() 
        print(line.strip())
        print(len(words))

if os.path.exists("merge.txt"):
    print("File exists")

else:
    print("File does not exist")

with open("science.txt","r") as f1:
    science = f1.read()
with open("maths.txt","r") as f2:
    maths = f2.read()

with open("merge.txt","w") as f3:
    f3.write(science)
    f3.write("\n")
    f3.write(maths)

print("Files merged")

if os.path.exists("merge.txt"):
    os.remove("merge.txt")
    print("File deleted")
else:
    print("File not found")