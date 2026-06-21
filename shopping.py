
filename = "shopping_list.txt"

initial_items = ["Apples\n", "Milk\n", "Bread\n"]

with open(filename, "w") as file:
    file.writelines(initial_items)

with open(filename, "r") as file:
    content = file.read()
    print(content)

new_items = ["Eggs\n", "Cheese\n"]

with open(filename, "a") as file:
    file.writelines(new_items)

with open(filename, "r") as file:
    for line in file:
        print(f"- {line.strip()}")