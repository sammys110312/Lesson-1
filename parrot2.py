class Parrot:
    species = "Senegal Parrot"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sing(self):
        print(self.name, "can sing Taylor Swift")
    def dance(self):
        print(self.name, "can dance")
p1 = Parrot("Dave", 13)
print(Parrot.species)
print(p1.name)
print(p1.age)
p1.sing()
p1.dance()