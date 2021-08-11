from random import randint

class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
        self.alive = True
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        pirate.health -= self.strength
        print("Sword attack!")
        print(f"{self.name} does {self.strength} damage against {pirate.name}")
        if pirate.health < 1:
            pirate.alive = False
            print(f"{pirate.name} has been killed!")
        return self

    def ai_move(self, pirate):
        self.attack(pirate)

class Shinobi(Ninja):

    def __init__(self, name):
        super().__init__(name)

    def throw_shuriken(self, pirate):
        die_roll = randint(1, 6)
        print("Shuriken attack!")
        if(die_roll + self.speed > pirate.speed + 2):
            pirate.health -= 30
            print("The ninja stars find their mark!")
            print(f"{self.name} does 30 damage against {pirate.name}")
            if pirate.health < 1:
                pirate.alive = False
                print(f"{pirate.name} has been killed!")
        else:
            print("Whoosh!")
        return self

    def ai_move(self, pirate):
        if self.health < 50:
            self.attack(pirate)
        else:
            die_roll = randint(1, 6)
            if die_roll > 3:
                self.throw_shuriken(pirate)
            else:
                self.attack(pirate)