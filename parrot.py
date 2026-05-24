class Parrot:
    species = "Senegal Parrot"
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = Parrot("Davvy",3)
p2 = Parrot("Filia", 2)
print(Parrot.species)
print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)