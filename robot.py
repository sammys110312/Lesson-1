class Robot:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
        print(f"Hello! I am {self.name}, a {self.model} model built in {self.year}.")
r1 = Robot("SALLY", "V", 2025)



