class Pet:
    def __init__(self, pet_name, tricks, health, energy, pet_type):
        self.pet_name = pet_name
        self.pet_type = pet_type
        self.energy = energy
        self.health = health
        self.tricks = tricks

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self, sound="contented sigh"):
        print(sound)
        return self

class Cat(Pet):
    def __init__(self, pet_name, tricks, health, energy, pet_type="Cat"):
        super().__init__(pet_name, tricks, health, energy, pet_type)

    def noise(self, sound="Meow!"):
        print(sound)
        return self

class Dog(Pet):
    def __init__(self, pet_name, tricks, health, energy, pet_type="Dog"):
        super().__init__(pet_name, tricks, health, energy, pet_type)

    def noise(self, sound="Bark!"):
        print(sound)
        return self