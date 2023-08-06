
import item
import scene
import random
import character

boots = 0


def mini_game():
    print("Let's play rock, paper, scissors!")
    move = ["rock", "paper", "scissors"]
    centaur_move = random.choice(move)

    choice = character.user_choice(
        "Would you play rock, paper, scissors?. (rock/paper/scissors) ",
        ["rock", "r", "paper", "p", "scissors", "s"]
    )
    print(f"You play {choice}! Centaur plays {centaur_move}!")

    if choice == centaur_move:
        print("It's a tie!")
        return "no"

    elif choice == "rock" or choice == "r":
        if centaur_move == "scissors":
            print("You win!")
            return "yes"
        else:
            print("You lose!")
            return "no"

    elif choice == "paper" or choice == "p":
        if centaur_move == "rock":
            print("You win!")
            return "yes"
        else:
            print("You lose!")
            return "no"

    elif choice == "scissors" or choice == "s":
        if centaur_move == "paper":
            print("You win!")
            return "yes"
        else:
            print("You lose!")
            return "no"

    else:
        return "An error occurred."


def centaur():
    print("You hear some music playing. You approach the music.\n"
          "You see a centaur and it spots you too.\n"
          "It happily strolls over to you and said:")
    result = mini_game()
    if boots == 0:
        if result == "yes":
            print("Congrats! Here's a free gift!")
            item.boots()
            scene.mid_scene()

        elif result == "no":
            print("Too bad! Better luck next time!")
            scene.mid_scene()
    else:
        if result == "yes":
            print("Congrats! I have nothing to give you but I hope this will help!")
            character.character_life += 1
            character.show_stats()
            scene.mid_scene()

        elif result == "no":
            print("Too bad! Better luck next time!")
            scene.mid_scene()