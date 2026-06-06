class Gallery:
    def __init__(self):
        self.art = []
        self.art.sort()
    def display_art(self):
        print("art in Gallery: ")
        for art in self.art:
            print(art)
    def add_art(self,art):
        self.art.append(art)
        self.art.sort()
        print(art, "added successfully")
    def lend_art(self,art):
        if art in self.art:
            self.art.remove(art)
            print("Art has been bought")
        else:
            print("Art not available")
s1 = Gallery()
while True:
    print("1. Display Art")
    print("2. Add Art")
    print("3. Buy Art")
    print("4. Exit")
    choice = int(input("What would you like to do: "))
    if choice == 1:
        s1.display_art()
    elif choice == 2:
        art = input("Enter art you would like to add: ")
        s1.add_art(art)
    elif choice == 3:
        art = input("Enter art you would like to bought: ")
        s1.lend_art(art)
    elif choice == 4:
        print("Thank you for visiting the Gallery")
        break
    else:
        print("Invalid choice")