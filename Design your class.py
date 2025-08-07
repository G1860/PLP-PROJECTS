# Base class: Superhero
class Superhero:
    def __init__(self, name, power, level):
        self.name = name
        self.power = power
        self.level = level
    
    def introduce(self):
        return f"I am {self.name}, and I have the power of {self.power}!"

    def fight(self):
        return f"{self.name} attacks with {self.power} at level {self.level}!"

# Derived class: FlyingSuperhero (inherits from Superhero)
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, level, flight_speed):
        super().__init__(name, power, level)
        self.flight_speed = flight_speed

    def fly(self):
        return f"{self.name} flies at {self.flight_speed} km/h!"

    # Overriding fight method (polymorphism)
    def fight(self):
        return f"{self.name} attacks from the sky with {self.power} at level {self.level}!"

# Object creation
hero1 = Superhero("Iron Shield", "Invincibility", 7)
hero2 = FlyingSuperhero("SkyFlash", "Lightning", 9, 500)

# Method testing
print(hero1.introduce())
print(hero1.fight())
print(hero2.introduce())
print(hero2.fly())
print(hero2.fight())
