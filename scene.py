
import character
import random

import pond
import test
import item
import trees
import centaur
import tent

rounds = 0


def check_winning_condition():
    global rounds
    if rounds == 5:
        print("You continue to press onwards through the dense and mysterious forest.\n"
              "The dense canopy above begins to thin and with every step forward,\n"
              "The once towering trees gradually give way to a vast, open landscape. \n"
              "You finally catch sight of unmistakable signs of human civilization. \n"
              "Your heart swells with relief, knowing that safety and comfort await. \n"
              "You escaped! You can finally rest. Congrats.")
        return False

    else:
        rounds += 1
        return True


def intro_scene():
    print("You stand in an unfamiliar forest, towering ancient trees loom overhead, \n"
          "their branches entwined like skeletal fingers reaching out to you.\n"
          "An eerie stillness surrounds you, broken only by the occasional rustle of leaves \n"
          "and the distant calls of mysterious creatures hidden in the shadows. \n"
          "Your goal is to escape this forest and to return home.")
    choice = character.user_choice(
        "Type continue to proceed. (continue) ",
        ["continue", "c"]
    )
    if choice == "continue" or choice == "c":
        print("You cautiously step foot into the dense, mysterious forest, \n"
              "uncertainty echoing with every rustle of leaves under your feet.")
        mid_scene()


def mid_scene():
    choice = character.user_choice(
        "Type continue to proceed or inventory to see your items and skills. (continue/inventory) ",
        ["continue", "c", "inventory", "i"]
    )
    if choice == "continue" or choice == "c":
        if check_winning_condition():
            phrases = [
                "You continue onwards.",
                "You push forward.",
                "You press ahead.",
                "You keep moving.",
                "You advance further.",
            ]
            phrase = random.choice(phrases)
            print(f"{phrase}")
            # test.combat()
            scenes_available = [
                pond.intro_pond,
                test.combat,
                trees.riddles_intro,
                centaur.centaur,
                tent.tent_intro
            ]
            chosen_scene = random.choice(scenes_available)
            # scenes_available.remove(chosen_scene)
            # because if rounds ever got minus (pond fairy scene)
            # scenes_available = [] aka empty
            # unless include if scenes_available = []
            # scenes_available is refreshed
            chosen_scene()

    elif choice == "inventory" or choice == "i":
        item.open_inventory()


def death_scene():
    print("Lost deep within the dense, unforgiving forest, you breathed your last breath, \n"
          "and the haunting whispers of the trees echoed a chilling truth: \n"
          "you shall never escape the clutches of the wilderness.")
    death()


def death_scene_drown():
    print("You take a leap into the glimmering pond. \n"
          "However, something feels different this time—almost suffocating.\n"
          "The waters that once embraced you with gentle enchantment now grip you with an unyielding force.\n"
          "You struggle to swim to the surface but an invisible force tugs you down.\n"
          "The need for air becomes overwhelming, and your vision fades to black.\n"
          "Perhaps this was the price of overindulgence.")
    death()


def death_scene_drink():
    print("Compelled by the overwhelming desire for power, you continue to drink from the pond. \n"
          "You feel a strange detachment from reality as time seems to blur.\n"
          "With each sip, your once-steady heartbeat races uncontrollably. \n"
          "Finally, your body collapses.")
    death()


def death_scene_trees():
    print("\"Wrong, wrong, all wrong. Your chances of escape mirror your wits — nonexistent.\"\n"
          "The figure mocks with a chilling echo before the very woods themselves appear\n"
          "to move towards you. Your vision starts to blur.\n"
          "You finally succumb to the encroaching void, \n"
          "your journey ending in an eerie unconsciousness within the heart of the suffocating woods.")
    death()


def death():
    print("Game over. Better luck next time.")


def escape_scene():
    phrases = ["With sheer determination and a burst of adrenaline,\n"
               "you managed to outwit the monstrous creature, \n"
               "escaping its clutches just in the nick of time.",
               "Summoning every ounce of courage, \n"
               "you cleverly diverted the monster's attention and slipped away, \n"
               "leaving it bewildered and defeated in your trail.",
               "In a daring display of agility and resourcefulness, \n"
               "you evaded the monster's relentless pursuit, \n"
               "disappearing into the shadows of the forest."]
    phrase = random.choice(phrases)
    print(f"{phrase}\n"
          "You have successfully escaped!")
    mid_scene()
