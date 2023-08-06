# Idea of this is that player encounters talking trees or something
# They ask the player some riddles
# The player can choose the answer from a set of options
# Around 3 riddles, if the player gets all of them correct
# Player gets a free item
# If player get 1 round, take 1 dmg etc.


import random
import character
import scene
import test
from test import Werewolf

correct_answers = 0


# Intro scene
def riddles_intro():
    print("As you enter deeper into the forest, the air grew heavy.\n"
          "The trees grew denser, further dimming the already sparse sunlight.\n"
          "Soon, the path ahead became so dark that you could barely see.")
    choice = character.user_choice(
        "Would you like to continue or leave? (continue/leave) ",
        ["continue", "c", "leave", "l"]
    )
    if choice == "continue" or choice == "c":
        print("You ignore the unsettling feelings and press onwards.\n"
              "Surely if you walk far enough, the darkness will clear up.")
        puzzle()

    elif choice == "leave" or choice == "l":
        leave()


def leave():
    print("You turn to retrace your steps.\n"
          "However each stride only seemed to carry you further into the darkness.\n"
          "The rustling of the leaves seemed to morph into mocking whispers.")
    choice = character.user_choice(
        "Would you like to try leaving again or give in? (leave/give up) ",
        ["leave", "l", "give up", "g"]
    )
    if choice == "leave" or choice == "l":
        print("Desperation fueled your attempts to escape from this place.\n"
              "Once some mere whispers, seemed to transform into sinister \n"
              "giggles that echoed through the trees. It was almost as if\n"
              "there were unseen eyes fixated upon you, \n"
              "finding amusement in your futile attempts.")
        puzzle()

    elif choice == "give up" or choice == "g":
        print("You acknowledge your situation, recognizing that escape was impossible.\n"
              "The whispers of the woods now held a sense of disappointment.")
        puzzle()


# Riddle
def present_riddle(riddle, options, correct_answer):
    print(riddle)

    # Shuffle the options
    random.shuffle(options)

    # Create a dictionary to map the original answer index to the shuffled index
    option_mapping = {i: option for i, option in enumerate(options, start=1)}

    # Display the shuffled options
    for i, option in option_mapping.items():
        print(f"{i}. {option}")

    # Get the player's choice and convert it back to the original answer index
    player_choice = int(input("Enter the number of your answer: "))
    if option_mapping[player_choice] == correct_answer:
        return True
    else:
        return False


def puzzle():

    global correct_answers
    print("Suddenly, two bright red glowing eyes materialized before you.\n"
          "A malicious grin etched across its ghastly visage.\n"
          "It said in a playful tone: \n"
          " 'You dare tread in my realm, and now you must pay the toll.\n"
          " Play my game of riddles, or forever become lost within these haunted woods.'")

    riddles = [
        {
            "riddle": "In the heart of the night, I crawl through your dreams. \n"
                      "My whispers of terror ignite silent screams. \n"
                      "What am I?",
            "options": ["A nightmare", "A specter", "A phantom", "A banshee"],
            "correct_answer": "A nightmare"
        },
        {
            "riddle": "When the moon is high and the winds do howl, \n"
                      "I emerge from the dark with a sinister scowl. \n"
                      "What am I?",
            "options": ["A werewolf", "A witch", "A demon", "A shadow"],
            "correct_answer": "A werewolf"
        },
        {
            "riddle": "In the misty graveyard, where the tombstones stand, \n"
                      "I roam with the lost souls, a skeletal hand. \n"
                      "What am I?",
            "options": ["Death", "A zombie", "A skeleton", "A reaper"],
            "correct_answer": "Death"
        },
        {
            "riddle": "As the moon's glow fades and the night grows cold, \n"
                      "I emerge from the darkness, tales of horror told. \n"
                      "What am I?",
            "options": ["A crypt keeper", "An ancient ghost", "A storyteller", "A banshee"],
            "correct_answer": "A storyteller"

        },
        {
            "riddle": "I'm cast by the light, a silhouette on the ground, \n"
                      "In the sun or the moon, I'm always around. \n"
                      "What am I?",
            "options": ["A ghost", "A specter", "A reflection", "A shadow"],
            "correct_answer": "A shadow"

        },
        {
            "riddle": "I'm the absence of light, where shadows reside, \n"
                      "In the deep of the night, I silently hide. \n"
                      "What am I?",
            "options": ["A shadow", "A void", "Darkness", "An abyss"],
            "correct_answer": "Darkness"
        }
    ]

    num_riddles_to_ask = 3  # Number of riddles to randomly ask

    selected_riddles = random.sample(riddles, num_riddles_to_ask)

    for riddle_data in selected_riddles:
        riddle = riddle_data["riddle"]
        options = riddle_data["options"]
        correct_answer = riddle_data["correct_answer"]

        if present_riddle(riddle, options, correct_answer):
            phrases = [
                "The figure's laughter rings out, 'Oh, look who's the genius!'",
                "Laughter cloaked in shadows fills the air as the figure jeers,\n"
                "'Congratulations, who knew you had such an extraordinary mind?",
                "The figure's sinister chuckle reverberates, 'Oh, brilliant deduction!"
            ]
            phrase = random.choice(phrases)
            print(f"{phrase}")
            correct_answers += 1
        else:
            phrases = [
                "As you answer, the figure's laughter crescendos into a cacophony of scorn,\n"
                "and in the shadows, unseen voices add their jeers to the haunting symphony.",
                "A choir of voices rose in unison, mocking the your answer with an eerie unity.",
                "Laughter, like dark whispers, fills the air. \n"
                "A sinister audience relish in your answer.",
            ]
            phrase = random.choice(phrases)
            print(f"{phrase}")

    results()


# Results
def results():

    global correct_answers

    if correct_answers == 0 or correct_answers == 1:
        scene.death_scene_trees()

    elif correct_answers == 2 or correct_answers == 3:
        print("With an unsettling smile, the figure said with a chilling melody, \n"
              "\"Impressive, you've earned your chance to leave! But before you do so..."
              "Please, enjoy my parting gift.\"\n"
              "The red glowing eyes vanished and the suffocating darkness of the woods gradually lifts.\n"
              "Just as you thought it was over, \n"
              "an earth-shaking roar rent the air, and a nightmarish werewolf burst forth.")
        correct_answers = 0
        test.combat_event(monster=Werewolf)

    else:
        print("An error occurred.")
