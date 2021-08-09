class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.pet_food = pet_food
        self.treats = treats
        self.pet = pet
        self.last_name = last_name
        self.first_name = first_name

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self