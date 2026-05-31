from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    def speak(self):
        print(f"{self.name} says: Woof!")

class Parrot(Animal):
    def __init__(self, name, colour):
        super().__init__(name)
        self.colour = colour
    def speak(self):
        print(f"{self.name} says: Squawk!")

class Lion(Animal):
    def __init__(self, name, pride_name):
        super().__init__(name)
        self.pride_name = pride_name
    def speak(self):
        print(f"{self.name} roars: Roar!")

s1 = Dog("Thor", 7)
s2 = Parrot("Dave", "Red")
s3 = Lion("Mufasa", "Ugandan Savannah Kings")

s1.speak()
s2.speak()
s3.speak()

print(s1.age)
print(s2.colour)
print(s3.pride_name)