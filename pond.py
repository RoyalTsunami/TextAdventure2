
import character
import random
import scene
import item
import test

drink = 0
jump = 0
blessed = None


def intro_pond():
    print("Along the forest path, you stumble upon a glimmering pond surrounded by luminous flowers.")
    choice = character.user_choice(
        "Would you like to explore the area or leave? (explore/leave) ",
        ["explore", "e", "leave", "l"]
    )
    if choice == "explore" or choice == "e":
        explore_pond()

    elif choice == "leave" or choice == "l":
        phrases = [
            "You decide to leave the area before exploring it further, \n"
            "wary of the potential dangers that may lie ahead.",
            "You decide that venturing further into the unknown might be too risky, so you back away.",
            "You opt not to explore the area further and continue your quest elsewhere.",
        ]
        phrase = random.choice(phrases)
        print(f"{phrase}")
        scene.mid_scene()


def explore_pond():
    print("You approach the pond.\n"
          "The surface shimmers with an otherworldly radiance.\n"
          "The allure of the enchanting pond's water tempts you.")
    pond_choice()


def explore_flowers():
    print("You decide to explore the mysterious flowers surrounding the glimmering pond,\n"
          "hoping they might hold some hidden secrets.")
    scene_choices = [fairy, monster]
    chosen_scene = random.choice(scene_choices)
    chosen_scene()


def monster():
    print("You venture deeper into the flower fields, when suddenly\n"
          "You find yourself whisked away to the forests depths once more by an unknown creature.")
    scene.rounds -= 2 if scene.rounds >= 2 else 1
    test.combat()


def fairy():
    global blessed
    if blessed is None:
        if random.random() < 0.5:
            blessed = True
            print("As you approach the radiant blooms, a dazzling light flickers amidst the petals,\n"
                  "revealing a captivating fairy fluttering gracefully before you.\n"
                  "It starts singing a mesmerizing melody which leaves you entranced.\n"
                  "When it stopped, its luminous form dissolves into the shadows.\n"
                  "You feel blessed.")
            character.character_speed += 1
            character.show_stats()
            flower_choice()
        else:
            print("You step into flowers, finding solace in its beauty and tranquility.\n"
                  "There are no hidden treasures or secrets to be uncovered here.")
            flower_choice()

    else:
        if random.random() < 0.5:
            print("As you step into the flower field, a playful giggle echoes through the trees.\n"
                  "Suddenly, a whimsical fairy materializes before you.\n"
                  "With a sly grin and a mischievous twinkle in her eyes, she twirls and vanishes.\n"
                  "Glittering particles surrounds you and you feel a sudden shift in reality.\n"
                  "You find yourself yet again beneath the dense forest with no clue of your location.")
            scene.rounds -= 2 if scene.rounds >= 2 else 1
            scene.mid_scene()

        else:
            print("You step into flowers, finding solace in its beauty and tranquility.\n"
                  "There are no hidden treasures or secrets to be uncovered here.")
            flower_choice()


def jump_pond():
    global jump
    if jump == 0:
        jump = 1
        character.character_strength += 2
        print("You take a deep breath and plunge headfirst into the glimmering pond.\n"
              "As you break through the surface, the magical waters embrace you like a gentle caress,\n"
              "filling your senses with a euphoric rush of power."
              f"Strength points is now {character.character_strength}")
        character.show_stats()
        pond_bottom()

    elif jump == 1:
        jump = 2
        print("The magical water engulfs you once more as you dive into the depths below.\n"
              "You explore every nook and crevice, but to your dismay, find nothing.\n"
              "Perhaps if you search it again, you'll find something helpful.")
        pond_choice()

    elif jump == 2:
        scene.death_scene_drown()

    else:
        print("An error has occurred.")


def drink_pond():
    global drink
    if drink == 0:
        drink = 1
        character.character_life += 3
        print("You decide to take a cautious sip. \n"
              "As the cool liquid touches your lips, you feel a wave of energy rushes through your body.\n"
              "You feel your weariness is replaced with newfound vigor.\n"
              f"Life points is now {character.character_life}")
        character.show_stats()
        pond_choice()

    elif drink == 1:
        drink = 2
        print("You drink more water. You feel quenched, but nothing extraordinary occurs.\n"
              "Perhaps you should give it another sip.")
        pond_choice()

    elif drink == 2:
        drink = 3
        print("You drink more water. The lingering taste of power on your lips beckons for more, \n"
              "promising greater abilities and untold wonders.\n"
              "Perhaps, just one more sip will unlock hidden potential and reveal secrets beyond imagination.")
        pond_choice()

    elif drink == 3:
        scene.death_scene_drink()

    else:
        print("An error has occurred.")


def pond_choice():
    choice = character.user_choice(
        "Would you like to jump inside the pond, drink the water, explore further or leave? \n"
        "(jump/drink/explore/leave) ",
        ["explore", "e", "leave", "l", "jump", "j", "drink", "d"]
    )
    if choice == "explore" or choice == "e":
        explore_flowers()

    elif choice == "leave" or choice == "l":
        phrases = [
            "You decide to leave the area before exploring it further, \n"
            "wary of the potential dangers that may lie ahead.",
            "You decide that venturing further into the unknown might be too risky, so you back away.",
            "You opt not to explore the area further and continue your quest elsewhere.",
        ]
        phrase = random.choice(phrases)
        print(f"{phrase}")
        scene.mid_scene()

    elif choice == "jump" or choice == "j":
        jump_pond()

    elif choice == "drink" or choice == "d":
        drink_pond()


def pond_bottom():
    print("In the depths of the pond, your eyes widen in astonishment.\n"
          "Amidst the sparkling radiance, you glimpse the faint outline of a mysterious object glinting below.\n"
          "You pick out the object and emerge from the water.")
    item.sword()
    pond_choice()


def flower_choice():
    choice = character.user_choice(
        "Would you like to go to the pond, explore further or leave? \n"
        "(pond/explore/leave) ",
        ["explore", "e", "leave", "l", "pond", "p"]
    )
    if choice == "explore" or choice == "e":
        explore_flowers()

    elif choice == "leave" or choice == "l":
        phrases = [
            "You decide to leave the area before exploring it further, \n"
            "wary of the potential dangers that may lie ahead.",
            "You decide that venturing further into the unknown might be too risky, so you back away.",
            "You opt not to explore the area further and continue your quest elsewhere.",
        ]
        phrase = random.choice(phrases)
        print(f"{phrase}")
        scene.mid_scene()
