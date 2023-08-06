
import character
import scene
import random
import pond, test, centaur, trees

inventory_items = []


def open_inventory():
    character.show_stats()
    show_inventory()
    choice = character.user_choice(
        "Type continue to return on your journey. (continue) ",
        ["continue", "c"]
    )
    if choice == "continue" or choice == "c":
        if scene.check_winning_condition():
            phrases = [
                "You continue onwards.",
                "You push forward.",
                "You press ahead.",
                "You keep moving.",
                "You advance further.",
            ]
            phrase = random.choice(phrases)
            print(f"{phrase}")
            # random scene plays out
            scenes_available = [pond.intro_pond, test.combat, trees.riddles_intro, centaur.centaur]
            chosen_scene = random.choice(scenes_available)
            chosen_scene()


def sword():
    print("You picked up a rusty sword. Your attack increased by 3.")
    character.character_strength += 3
    character.show_stats()
    inventory_items.append("Rusty Sword")
    show_inventory()


def show_inventory():
    print(f"Inventory Items: {inventory_items}")


def boots():
    print("You obtain speedy boots. Your speed increased by 3.")
    character.character_speed += 3
    character.show_stats()
    inventory_items.append("Speedy Boots")
    show_inventory()
