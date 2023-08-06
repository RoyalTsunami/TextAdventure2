def user_choice(prompt, options):
    while True:
        choice = input(prompt).lower().strip()
        if choice in options:
            print("=" * 100)
            return choice
        print("Invalid choice. Try again.")


character_name = None
character_strength = None
character_speed = None
character_life = None


def create_character():
    global character_name
    character_name = input("""
Let's start by giving your character a name.
What is your character name? """)
    character_skill()


def character_skill():
    global character_strength, character_life, character_speed
    print("""
Now let's determine your character's skills, which you will use throughout the game.
In this game, your character has three skills:

- Strength, which you will use in combat or any strength test
    > The amount of life points lost by monster is determined by your strength

- Speed, which you will use to escape dangerous situations
    > You can escape monsters only if your speed is higher than the monster's.
    
- Life, which determines your life energy
    > Points will be lost when hurt 
    > Whenever Life reaches 0, your character dies and the game is over.


Later, you will be given points to increase your skills.

Here is your base Character Skills Sheet:
    """)

    character_strength = 1
    character_speed = 1
    character_life = 15

    show_stats()

    choice = user_choice(
        "Type continue to proceed. (continue) ",
        ["continue", "c", "d"]
    )
    if choice == "continue" or choice == "c":
        modify_skill()

    elif choice == "d":
        character_life = 99
        character_speed = 99
        character_strength = 99
        show_stats()


def show_stats():
    print(f"""
        Name: {character_name}
        Strength: {character_strength}
        Speed: {character_speed}
        Life: {character_life}
        """)


def modify_skill():
    global character_strength, character_life, character_speed
    points = 5
    print(f"""
You are given {points} points. Please assign the number of points to each skill.
Each single assigned point increases the respective base Character Skills by 1.
    """)
    valid = None
    while valid is None:
        free_points = list(map(str, range(0, points + 1)))
        strength = user_choice(
            f"Type the amount of points you want to assign to strength. (Points available: {points}) ",
            free_points
        )
        check = user_choice(
            f"Are you sure you want to assign {strength} points to strength? (yes/no) ",
            ["yes", "no"]
        )
        if check == "yes":
            valid = "yes"
            character_strength = int(character_strength) + int(strength)
            points = int(points) - int(strength)

    if points > 0:
        valid = None
        while valid is None:
            free_points = list(map(str, range(0, points + 1)))
            speed = user_choice(
                f"Type the amount of points you want to assign to speed. (Points available: {points}) ",
                free_points
            )
            check = user_choice(
                f"Are you sure you want to assign {speed} points to speed? (yes/no) ",
                ["yes", "no"]
            )
            if check == "yes":
                valid = "yes"
                character_speed = int(character_speed) + int(speed)
                points = int(points) - int(speed)

    if points > 0:
        print(f"""
    You have {points} points remaining, this will automatically be added to your life.
        """)

        character_life = int(character_life) + int(points)

    else:
        print("""
You have no more points remaining.
    """)

    print("""
This is your current character skills.
    """)
    show_stats()
