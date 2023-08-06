
import scene
import character
import random
import test
from test import Ghost

food_supplies = 1
nap = 0


def tent_intro():
    print("You see a tent in the distance.")
    choice = character.user_choice(
        "Would you like to explore the area or leave? (explore/leave) ",
        ["explore", "e", "leave", "l"]
    )
    if choice == "explore" or choice == "e":
        explore_tent()

    elif choice == "leave" or choice == "l":
        phrases = [
            "Leaving the tent untouched seems like the right choice.",
            "Leaving the tent be might be the smart move.",
            "You decide it's a good idea to steer clear of the tent.",
        ]
        phrase = random.choice(phrases)
        print(f"{phrase} You leave the area.")
        scene.mid_scene()


def explore_tent():
    print("You decide to explore the tent.\n"
          "You open the tent and see a sleeping bag.\n"
          "Next to it were cans of food and bottles of water. \n"
          "You wonder what had compelled the tent's owner to abandon \n"
          "their tent so abruptly even leaving their supplies behind.\n"
          )
    choice = character.user_choice(
        "Would you like to rest in the tent or leave? (rest/leave) ",
        ["rest", "r", "leave", "l"]
    )
    if choice == "rest" or choice == "r":
        rest()

    elif choice == "leave" or choice == "l":
        phrases = [
            "You decide leaving this tent alone is probably best.",
            "This tent looks abandoned for a reason — resting inside isn't wise.",
            "Something tells you sleeping here could be a mistake.",
        ]
        phrase = random.choice(phrases)
        print(f"{phrase} You leave the tent.")
        scene.mid_scene()


def rest():
    print("You lay on the sleeping bag.")
    choice = character.user_choice(
        "Would you like to take a nap, consume the food supplies or leave? (nap/consume/leave) ",
        ["nap", "n", "consume", "c", "leave", "l"]
    )
    if choice == "nap" or choice == "n":
        nap_tent()

    elif choice == "consume" or choice == "c":
        consume()

    elif choice == "leave" or choice == "l":
        phrases = [
            "You decide it's probably not a good idea to relax here or eat the food.",
            "Napping or eating this food might have some risks you don't know about.",
            "Taking a nap or eating from these supplies in this situation is not a wise choice.",
        ]
        phrase = random.choice(phrases)
        print(f"{phrase} You leave the area.")
        scene.mid_scene()


def nap_tent():
    global nap
    nap += 1
    if nap == 0:
        print("You decided to take a nap.\n"
              "You wake up after a few hours feeling refreshed.\n"
              "Your life points increased by 4.")
        character.character_life += 4
        character.show_stats()
        menu()

    elif nap == 1:
        print("You decide to take another nap.\n"
              "Who knows, this may be the very last chance you get to have a peaceful sleep.\n"
              "You wake up feeling refreshed.\n"
              "Stretching you feel as if unseen gaze watching you.\n"
              "You look around only to find the stillness of the forest.\n"
              "Your life points increased by 3.")
        character.character_life += 3
        character.show_stats()
        menu()

    elif nap == 2:
        print("You decide to take yet another nap.\n"
              "Because why not.\n"
              "Abruptly, you get woken up by a cold, frigid hand gripping your shoulder.\n"
              "You find yourself staring into the hollow eyes of a shadowy figure.\n"
              "It screeches at you. You take 2 damage.")
        character.character_life -= 2
        character.show_stats()
        test.combat_event(monster=Ghost)


def consume():
    global food_supplies
    print("You cautiously sampled the cans of food and bottles of water.\n"
          "Surprisingly, the provisions appeared to be in decent condition.\n"
          "Your hunger gradually subsided as I finished the meal and quenched my thirst.\n"
          "Your life points increased by 2. ")
    character.character_life += 2
    character.show_stats()
    food_supplies = 0
    menu()


def menu():
    if food_supplies == 1 and nap == 1:
        choice = character.user_choice(
            "Would you like to take another nap, consume the food supplies or leave? \n"
            "(nap/consume/leave) ",
            ["nap", "n", "consume", "c", "leave", "l"]
        )
        if choice == "nap" or choice == "n":
            nap_tent()

        elif choice == "consume" or choice == "c":
            consume()

        elif choice == "leave" or choice == "l":
            phrases = [
                "You decided it was time to move on from the tent and explore further.",
                "You emerged from the tent, ready to continue your journey.",
                "You decided that you shouldn't waste more time resting and move on.",
            ]
            phrase = random.choice(phrases)
            print(f"{phrase} You leave the area.")
            scene.mid_scene()

    elif food_supplies == 0 and nap == 0:
        choice = character.user_choice(
            "Would you like to take a nap, consume the food supplies or leave?\n"
            "(nap/consume/leave) ",
            ["nap", "n", "consume", "c", "leave", "l"]
        )
        if choice == "nap" or choice == "n":
            nap_tent()

        elif choice == "consume" or choice == "c":
            print("There is no more food or water supplies laying around.\n"
                  "Glutton >:(")
            menu()

        elif choice == "leave" or choice == "l":
            phrases = [
                "You decided it was time to move on from the tent and explore further.",
                "You emerged from the tent, ready to continue your journey.",
                "You decided that you shouldn't waste more time resting and move on.",
            ]
            phrase = random.choice(phrases)
            print(f"{phrase} You leave the area.")
            scene.mid_scene()

    elif food_supplies == 0 and nap > 0:
        choice = character.user_choice(
            "Would you like to take another nap, consume the food supplies or leave? \n"
            "(nap/consume/leave) ",
            ["nap", "n", "consume", "c", "leave", "l"]
        )
        if choice == "nap" or choice == "n":
            nap_tent()

        elif choice == "consume" or choice == "c":
            print("There is no more food or water supplies laying around.\n"
                  "Glutton >:(")
            menu()

        elif choice == "leave" or choice == "l":
            phrases = [
                "You decided it was time to move on from the tent and explore further.",
                "You emerged from the tent, ready to continue your journey.",
                "You decided that you shouldn't waste more time resting and move on.",
            ]
            phrase = random.choice(phrases)
            print(f"{phrase} You leave the area.")
            scene.mid_scene()
