import scene
import character
# consider import textwrap next time :D
# usage:
# description = """You find yourself in a vast, ancient forest.
#                   Sunlight filters through the dense canopy above,
#                   casting dappled shadows on the forest floor.
#                   Birds chirp in the distance, and a gentle breeze
#                   rustles the leaves. The air is filled with an earthy
#                   scent, and you can't help but feel a sense of wonder
#                   and mystery in this enchanted place."""
# wrapped_description = textwrap.fill(description, width=60)
# print(wrapped_description)

play = character.user_choice(
    "Would you like to play? (yes/no) ",
    ["yes", "no"]
)

if play == "yes":
    character.create_character()
    print("Now you may begin your adventure. Good luck " + character.character_name + ".")
    scene.intro_scene()

else:
    print("That's too bad.")
