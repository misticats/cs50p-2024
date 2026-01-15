import random
import cowsay
import pyttsx3

class Player:
    def __init__(self, chosen_class):
        if chosen_class == "Adventurer": # Default
            self._health = random.randint(500, 1500)
            self._power = random.randint(50, 150)
            self._defense = random.randint(25, 75)
            self._accuracy = random.randint(25, 75)
            self._agility = random.randint(25, 75)
        elif chosen_class == "Warrior": #  hp+, atk~, def+, acc-, agi-
            self._health = random.randint(1000, 1500)
            self._power = random.randint(50, 150)
            self._defense = random.randint(50, 100)
            self._accuracy = random.randint(25, 50)
            self._agility = random.randint(25, 50)
        elif chosen_class == "Mage": # hp~, atk++, def-, acc-, agi~
            self._health = random.randint(500, 1000)
            self._power = random.randint(150, 200)
            self._defense = random.randint(25, 50)
            self._accuracy = random.randint(25, 50)
            self._agility = random.randint(25, 75)
        elif chosen_class == "Archer": # hp~, atk-, def-, acc+, agi+
            self._health = random.randint(500, 1000)
            self._power = random.randint(50, 100)
            self._defense = random.randint(25, 50)
            self._accuracy = random.randint(50, 75)
            self._agility = random.randint(50, 75)
        self._skill3 = "Counter"
        self._skill4 = "Dodge & Recover"

    def __str__(self):
        return (
            f"\nYour stats are: \n"
            f"HP: {self._health} \n"
            f"Power: {self._power} (Attack Power)\n"
            f"Defense: {self._defense} (Damage Mitigation)\n"
            f"Accuracy: {self._accuracy} (Chance to land attacks)\n"
            f"Agility: {self._agility} (Chance to counter/dodge attacks)\n"
        )

class Adventurer(Player):
    def __init__(self, chosen_class):
        super().__init__(chosen_class)
        self._skill1 = "Swift Strike"
        self._skill2 = "Focus Strike"

class Warrior(Player):
    def __init__(self, chosen_class):
        super().__init__(chosen_class)
        self._skill1 = "Heavy Slash"
        self._skill2 = "Shield Bash"

class Mage(Player):
    def __init__(self, chosen_class):
        super().__init__(chosen_class)
        self._skill1 = "Fireball"
        self._skill2 = "Blizzard"

class Archer(Player):
    def __init__(self, chosen_class):
        super().__init__(chosen_class)
        self._skill1 = "Quick Shot"
        self._skill2 = "Arrow Rain"

class Monster:
    def __init__(self):
        self.health = random.randint(500, 1500)
        self.defense = random.randint(0, 40)

    def normal_attack(self, player_defense):
        return max(random.randint(0, 100) - player_defense, 0)

    def special_attack(self, player_defense):
        return max(random.randint(0, 200) - player_defense, 0)


def main():
    chosen_class = choose_class()
    if chosen_class == "Adventurer":
        player = Adventurer(chosen_class)
    elif chosen_class == "Warrior":
        player = Warrior(chosen_class)
    elif chosen_class == "Mage":
        player = Mage(chosen_class)
    elif chosen_class == "Archer":
        player = Archer(chosen_class)
    print(player)
    battle(player)


def choose_class():
    # Prompt user for class and validate
    available_classes = ["Adventurer", "Warrior", "Mage", "Archer"]
    print("Available classes:")
    for i, class_name in enumerate(available_classes):
        print(f"{i + 1}. {class_name}")

    while True:
        chosen_input = input("Choose your class (by number or name): ").strip()

        # Handle numeric input
        if chosen_input.isdigit():
            chosen_index = int(chosen_input) - 1
            if 0 <= chosen_index < len(available_classes):
                return available_classes[chosen_index]
            else:
                print(f"{chosen_input} is not a valid choice. Please try again.")

        # Handle name input
        else:
            chosen_class = chosen_input.capitalize()
            if chosen_class in available_classes:
                return chosen_class
            else:
                print(f"{chosen_input} is not a valid choice. Please try again.")


def battle(player):
    monster = Monster()
    tts_engine = pyttsx3.init()

   # Setting English narrator voice
    voices = tts_engine.getProperty('voices')
    for voice in voices:
        if 'english' in voice.name.lower() or 'en' in voice.id.lower():
            tts_engine.setProperty('voice', voice.id)
            break

    # Monster ASCII Art
    print("A monster appears!")
    cowsay.cow("Let's battle! ")
    tts_engine.say("A monster appears! MOOOOOO")
    tts_engine.runAndWait()

    # Battle Loop
    while player._health > 0 and monster.health > 0:
        # Display Player's HP
        print(f"\nPlayer HP: {player._health}")
        print(f"Monster HP: {monster.health}")

        # ASCII Table for Abilities
        print("┌─────────────────────")
        print(f"| 1: {player._skill1} ")
        print(f"| 2: {player._skill2} ")
        print("| 3: Counter          ")
        print("| 4: Dodge & Recover  ")
        print("└─────────────────────")


        choice = get_player_choice()

        # Constructing the message based on player's choice
        skill_name = ""
        if choice == 1:
            skill_name = player._skill1
        elif choice == 2:
            skill_name = player._skill2
        elif choice == 3:
            skill_name = player._skill3
        elif choice == 4:
            skill_name = player._skill4

        # Handling player's action
        success, damage = handle_player_action(choice, player, monster)

         # Handling player's action for the first cow
        if choice in [1, 2]:  # Normal attacks
            attack_message = f"Player uses {skill_name}!"
            cowsay.cow(attack_message)
            tts_engine.say(attack_message)
            tts_engine.runAndWait()

            if success:
                attack_message = f"Player attack landed! Dealing {damage} damage."
            else:
                attack_message = "Player attack missed!"
        elif choice in [3, 4]:  # Special abilities
            attack_message = f"Player prepares to {skill_name}!"

        cowsay.cow(attack_message)
        tts_engine.say(attack_message)
        tts_engine.runAndWait()

        # Handling monster's action for the second cow
        monster_action = random.choices([1, 2, 3], weights=(50, 20, 30))[0]
        monster_message = monster_attack(player, monster, monster_action, choice, tts_engine)
        cowsay.cow(monster_message)
        tts_engine.say(monster_message)
        tts_engine.runAndWait()

        print("============================================================")

        # Check for end of battle
        check_end_of_battle(player, monster, tts_engine)



def get_player_choice():
    while True:
        try:
            choice = int(input("Choose your ability: "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("Invalid choice. Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def handle_player_action(choice, player, monster):
    original_power = player._power
    original_accuracy = player._accuracy

    if choice == 1:
        success, damage = player_attack(player, monster)
        if success:
            # Reduce monster's health by the damage dealt
            monster.health -= damage
    elif choice == 2:
        # Enhanced attack: Increase damage by 1.5 and reduce accuracy by 50%
        player._power = int(player._power * 1.5)
        player._accuracy = int(player._accuracy * 0.5)
        success, damage = player_attack(player, monster)
        if success:
            # Reduce monster's health by the damage dealt
            monster.health -= damage
        # Restore original power and accuracy
        player._power, player._accuracy = original_power, original_accuracy
    else:
        # Counter or Dodge & Recover, no immediate attack occurs
        success, damage = False, 0

    return success, damage


def player_attack(player, monster):
    if random.randint(0, 100) < player._accuracy:
        return True, player._power
    else:
        return False, 0


def monster_attack(player, monster, monster_action, player_choice, tts_engine):
    monster_power = random.randint(50, 150)  # Cow's power is randomly generated each turn

    if monster_action in [1, 2]:  # Monster attacks
        attack = monster_power
        if player_choice in [1, 2]:  # Normal attacks
            attack -= player._defense

        player_hit = monster_power > player._agility
        if player_hit:
            player._health -= attack
            return f"Cow's attack landed! Dealing {attack} damage."
        else:
            if player_choice == 3:  # Counter
                counter_damage = monster_power  # Damage dealt back to the cow
                monster.health -= counter_damage
                return f"Cow's attack missed! You countered successfully, dealing {counter_damage} damage."
            elif player_choice == 4:  # Dodge & Recover
                recovery_amount = random.randint(50, 200)
                player._health = min(player._health + recovery_amount, 1500)
                return f"Cow's attack missed! You dodged and recovered {recovery_amount} health."

    else:
        return "Cow does nothing."


def await_monster_move(player, monster, player_choice, tts_engine):
    # This function will handle the player's move when using Counter or Dodge & Recover
    # Monster's turn
    monster_action = random.choices([1, 2, 3], weights=(50, 20, 30))[0]
    monster_message = monster_attack(player, monster, monster_action, player_choice, tts_engine)
    cowsay.cow(monster_message)
    tts_engine.runAndWait()


def check_end_of_battle(player, monster, tts_engine):
    if player._health <= 0:
        game_over_message = "==================\nYOU LOST, GAME OVER\n=================="
        print(game_over_message)
        tts_engine.say("You lost, game over")
        tts_engine.runAndWait()
    elif monster.health <= 0:
        victory_message = "====================\nVICTORY! YOU WON!\n===================="
        print(victory_message)
        tts_engine.say("Victory! You won!")
        tts_engine.runAndWait()


if __name__ == "__main__":
    main()
