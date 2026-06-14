from abc import ABC, abstractmethod

class Instrument(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

class Guitar(Instrument):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return "Strum! Twang!"

class Drum(Instrument):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return "Boom! Rat-a-tat!"

instruments = [Guitar("Acoustic"), Drum("Snare")]

for inst in instruments:
    print(f"The {inst.name} goes: {inst.make_sound()}")