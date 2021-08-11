from random import randint, random

class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100
        self.alive = True

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        ninja.health -= self.strength
        print("Cutlass attack!")
        print(f"{self.name} does {self.strength} damage against {ninja.name}")
        if ninja.health < 1:
            ninja.alive = False
            print(f"{ninja.name} has been killed!")
        return self

    def ai_move(self, ninja):
        self.attack(ninja)


class Grenadier(Pirate):

    def __init__(self, name):
        super().__init__(name)

    def throw_grenade(self, ninja):
        die_roll = randint(1, 6)
        if die_roll + self.speed > ninja.speed + 3:
            saving_throw = randint(1, 6)
            if saving_throw + 4 <= ninja.speed:
                print("The ninja dodges and only takes half damage!")
                print(f"{self.name} does 25 damage against {ninja.name}")
                ninja.health -= 25
                if ninja.health < 1:
                    ninja.alive = False
                    print(f"{ninja.name} has been killed!")
            else:
                print("BOOM!")
                print(f"{self.name} does 50 damage against {ninja.name}")
                ninja.health -= 50
                if ninja.health < 1:
                    ninja.alive = False
                    print(f"{ninja.name} has been killed!")
        elif die_roll == 1:
            print("Clumsy pirate!")
            saving_throw = randint(1, 6)
            if(saving_throw <= self.speed):
                print("Ye fumbled ye grenade but avoided a nasty burn! Half damage!")
                print(f"{self.name} loses 25 health")
                self.health -= 25
                if self.health < 1:
                    self.alive = False
                print(f"{self.name} has died of self-inflicted wounds!")
            else:
                print("Ye hath nearly blown yerself to bits!")
                print(f"{self.name} loses 50 health")
                self.health -= 50
                if self.health < 1:
                    self.alive = False
                    print(f"{self.name} has actually blown themselves up!")
        else:
            print("Curses! Ye missed!")
        return self

    def ai_move(self, ninja):
        if self.health < 60:
            self.attack(ninja)
        else:
            die_roll = randint(1, 6)
            if die_roll > 4:
                self.throw_grenade(ninja)
            else:
                self.attack(ninja)


