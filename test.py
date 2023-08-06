import random
import character
import scene


def combat():
    monster_choices = [Slime, Goblin, Troll, Spider, Serpent]
    chosen_monster = random.choice(monster_choices)()
    print(f"You encountered a {chosen_monster.name}!")
    chosen_monster.show_monster_stat()

    while True:
        choice = character.user_choice(
            "Would you like to fight or run away? (fight/run) ",
            ["fight", "f", "run", "r"])
        if choice == "fight" or choice == "f":
            print(f"You attack the monster, dealing {character.character_strength} damage.")
            chosen_monster.hp = int(chosen_monster.hp) - int(character.character_strength)

            if chosen_monster.hp > 0:
                print(f"The {chosen_monster.name} has {chosen_monster.hp} health remaining.")
                chosen_monster.atk_move()
                character.character_life = int(character.character_life) - int(chosen_monster.atk_dmg)

                if character.character_life > 0:
                    print(f"You have {character.character_life} health remaining.")

                else:
                    print(f"You have been slain by {chosen_monster.name}. Better luck next time.")
                    scene.death_scene()
                    break

            else:
                print(f"You have slain the {chosen_monster.name}!")
                scene.mid_scene()
                break

        elif choice == "run" or choice == "r":
            escape_success = chosen_monster.escape_move()
            if escape_success:
                scene.escape_scene()
                break

            else:
                chosen_monster.atk_move()
                character.character_life = int(character.character_life) - int(chosen_monster.atk_dmg)
                if character.character_life > 0:
                    print(f"You have {character.character_life} health remaining.")

                else:
                    print(f"You have been slain by {chosen_monster.name}. Better luck next time.")
                    scene.death_scene()
                    break


class Monster:
    def __init__(self,
                 name,
                 hp_range,
                 dmg_range,
                 spd_range):
        self.name = name
        self.hp = random.randint(*hp_range)
        self.atk_dmg = random.randint(*dmg_range)
        self.spd = random.randint(*spd_range)

    def show_monster_stat(self):
        print(f"""
            Name: {self.name}
            Strength: {self.atk_dmg}
            Speed: {self.spd}
            Life: {self.hp}
            """)

    def atk_move(self, atk_phrase):
        min_atk = self.atk_dmg - 2 if self.atk_dmg > 2 else 1
        atk_dmg = random.randint(min_atk, self.atk_dmg)
        phrase = random.choice(atk_phrase)
        print(f"{self.name} {phrase} You take {atk_dmg} damage!")

    def get_hurt(self, dmg):
        self.hp -= dmg
        print(f"You attack the {self.name}, dealing {dmg} damage!")

    def escape_move(self):
        chance = character.character_speed / self.spd
        if chance >= 1:
            return True

        else:
            if random.random() < chance:
                return True
            else:
                print(f"You failed to escape. The {self.name} attacks!")
                return False


class Slime(Monster):
    def __init__(self):
        super().__init__(name="Slime",
                         hp_range=(3, 6),
                         dmg_range=(1, 2),
                         spd_range=(1, 2))

    def atk_move(self, **kwargs):
        atk_phrase = ["jumps on you and squishes you!",
                      "shoots a trail of slime at you!",
                      "bounces around and slams into you!"]
        super().atk_move(atk_phrase)


class Goblin(Monster):
    def __init__(self):
        super().__init__(name="Goblin",
                         hp_range=(5, 7),
                         dmg_range=(2, 4),
                         spd_range=(3, 6))

    def atk_move(self, **kwargs):
        atk_phrase = ["throws a jagged rock at you!",
                      "fires a crude arrow from its bow, hitting you!",
                      "swiftly slashes its claws across your chest!"]
        super().atk_move(atk_phrase)


class Troll(Monster):
    def __init__(self):
        super().__init__(name="Troll",
                         hp_range=(7, 10),
                         dmg_range=(4, 6),
                         spd_range=(1, 3))

    def atk_move(self, **kwargs):
        atk_phrase = ["picks up a boulder and hurls it at you!",
                      "swings its massive wooden club, crushing you with brute force!",
                      "picks up a boulder and hurls it at you!"]
        super().atk_move(atk_phrase)


class Spider(Monster):
    def __init__(self):
        super().__init__(name="Giant Spider",
                         hp_range=(3, 6),
                         dmg_range=(1, 3),
                         spd_range=(4, 6))

    def atk_move(self, **kwargs):
        atk_phrase = ["lunges forward, sinking its venomous fangs deep into your leg!",
                      "shoots a sticky web from its spinnerets, entangling you!",
                      "releases a cloud of poisonous spores!"]
        super().atk_move(atk_phrase)


class Serpent(Monster):
    def __init__(self):
        super().__init__(name="Serpent",
                         hp_range=(2, 8),
                         dmg_range=(3, 4),
                         spd_range=(4, 6))

    def atk_move(self, **kwargs):
        atk_phrase = ["coils around your body, constricting tightly!",
                      "spews a stream of corrosive venom at you!",
                      "spews a stream of corrosive venom at you!"]
        super().atk_move(atk_phrase)


class Werewolf(Monster):
    def __init__(self):
        super().__init__(name="Werewolf",
                         hp_range=(7, 10),
                         dmg_range=(4, 6),
                         spd_range=(3, 5))

    def atk_move(self, **kwargs):
        atk_phrase = ["lunges forward and slashes you with its razor-sharp claws!",
                      "snaps its jaws and sink its sharp teeth into your flesh!",
                      "grabs hold of you and hurls you forcefully to the ground!"]
        super().atk_move(atk_phrase)


class Ghost(Monster):
    def __init__(self):
        super().__init__(name="Ghost",
                         hp_range=(7, 10),
                         dmg_range=(3, 5),
                         spd_range=(4, 6))

    def atk_move(self, **kwargs):
        atk_phrase = ["emits a blood-curdling wail that pierces the air!",
                      "phases through you, draining your life force!",
                      "traps you in a vortex, disorienting you!"]
        super().atk_move(atk_phrase)


def combat_event(monster):
    chosen_monster = monster()
    print(f"You encountered a {chosen_monster.name}!")
    chosen_monster.show_monster_stat()

    while True:
        choice = character.user_choice(
            "Would you like to fight or run away? (fight/run) ",
            ["fight", "f", "run", "r"])
        if choice == "fight" or choice == "f":
            print(f"You attack the monster, dealing {character.character_strength} damage.")
            chosen_monster.hp = int(chosen_monster.hp) - int(character.character_strength)

            if chosen_monster.hp > 0:
                print(f"The {chosen_monster.name} has {chosen_monster.hp} health remaining.")
                chosen_monster.atk_move()
                character.character_life = int(character.character_life) - int(chosen_monster.atk_dmg)

                if character.character_life > 0:
                    print(f"You have {character.character_life} health remaining.")

                else:
                    print(f"You have been slain by {chosen_monster.name}. Better luck next time.")
                    scene.death_scene()
                    break

            else:
                print(f"You have slain the {chosen_monster.name}!")
                scene.mid_scene()
                break

        elif choice == "run" or choice == "r":
            escape_success = chosen_monster.escape_move()
            if escape_success:
                scene.escape_scene()
                break

            else:
                chosen_monster.atk_move()
                character.character_life = int(character.character_life) - int(chosen_monster.atk_dmg)
                if character.character_life > 0:
                    print(f"You have {character.character_life} health remaining.")

                else:
                    print(f"You have been slain by {chosen_monster.name}. Better luck next time.")
                    scene.death_scene()
                    break
