from Python_OOP.Dojo_Pets.Pet import Dog
from Python_OOP.Dojo_Pets.Ninja import Ninja

kennie = Dog(pet_name="Kennie", tricks=None, energy=200, health=100)
stuart = Ninja(first_name="Stuart", last_name="Yee", pet=kennie, treats="bone", pet_food="chicken")

stuart.feed().walk().bathe()

print(f"Energy is {kennie.energy}")
print(f"Health is {kennie.health}")








