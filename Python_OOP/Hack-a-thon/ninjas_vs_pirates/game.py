from classes.ninja import Ninja, Shinobi
from classes.pirate import Pirate, Grenadier
from random import randint

def intro():
    pirates = [Pirate("Jack Sparrow"), Grenadier("Bomby")]
    ninjas = [Ninja("Donatello"), Shinobi("Ryu")]

    print("The battle has begun! Here are the fighters:")
    print("Ninjas:")
    for ninja in ninjas:
        ninja.show_stats()
    print("Pirates:")
    for pirate in pirates:
        pirate.show_stats()
    players = (pirates, ninjas)
    game = (1, players)

    pause()
    return game

def pause():
    x = input("Press ENTER to continue ")
    print("Continued...")

def round(game):
    round_num = game[0]
    players = game[1]
    pirates = players[0]
    ninjas = players[1]
    print(f"Round {round_num}!")
    for i in range(2):
        if ninjas[i].alive == True:
            coin_flip = randint(0,1)
            foe = pirates[coin_flip]
            while foe.alive == False:
                if pirates[0].alive == False & pirates[1].alive == False:
                    break
                coin_flip = randint(0, 1)
                foe = pirates[coin_flip]
            if foe.alive == False:
                break
            ninjas[i].ai_move(foe)
    for i in range(2):
        if pirates[i].alive == True:
            coin_flip = randint(0,1)
            foe = ninjas[coin_flip]
            while foe.alive == False:
                if ninjas[0].alive == False & ninjas[1].alive == False:
                    break
                coin_flip = randint(0, 1)
                foe = ninjas[coin_flip]
            if foe.alive == False:
                break
            pirates[i].ai_move(foe)
    print("Ninjas:")
    for ninja in ninjas:
        ninja.show_stats()
    print("Pirates:")
    for pirate in pirates:
        pirate.show_stats()
    round_num += 1
    game = (round_num, players)
    pause()
    return game

def between_rounds(game):
    players = game[1]
    pirates = players[0]
    ninjas = players[1]
    team_pirate = 0
    team_ninja = 0

    for pirate in pirates:
        if pirate.alive == True:
            team_pirate += 1

    for ninja in ninjas:
        if ninja.alive == True:
            team_ninja += 1

    if team_pirate == 0:
        print("All pirates are dead, the Ninjas win!")
        resolution = (0,0)
        return resolution
    elif team_ninja == 0:
        print("All ninjas are dead, the pirates win!")
        resolution = (0, 0)
        return resolution
    else:
        return game

def run_game():
    game_in_progress = round(intro())
    between_rounds(game_in_progress)

    while game_in_progress[0] > 0:
        this_round = round(game_in_progress)
        game_in_progress = between_rounds(this_round)


if __name__ == "__main__":
    run_game()
