
# RPG ASCII Battle
#### Description:
RPG ASCII Battle is a small, turn-based RPG played entirely in the terminal. It’s written in Python and uses simple ASCII visuals, with some inspiration from classic games like Pokémon.

Each run is a little different thanks to randomized stats and damage, so you’re not playing the exact same game every time. The focus is on straightforward mechanics, experimentation, and having fun with core RPG ideas rather than flashy graphics.


### Key Features:
- **Class Selection**: Start your adventure by choosing one of four unique classes: Adventurer, Warrior, Mage, or Archer. Each class plays a bit differently and comes with its own abilities.
- **Turn-Based Combat**: Battles are fully turn-based, giving you time to think about what to do next instead of relying on fast reactions.
- **Special Abilities**: Every class has special abilities that can change how fights play out and help you survive tougher encounters.
- **ASCII-Art**: Monsters and battle scenes are displayed using ASCII art via the cowsay module, giving the game a lighthearted, retro feel.
- **Narrated Battle**: The game can narrate battles using pyttsx3, which adds a bit of personality and makes fights feel more alive.
- **Dynamic Gameplay**: Thanks to the 'random' module, each game session is unpredictable. Randomized stats and damage mean that no two playthroughs are exactly the same.


### Project Structure and Design Choices
- **'Player' and 'Monster' Classes**: The game logic is built around Player and Monster classes, which keep stats, abilities, and behavior organized and easy to extend.
- **Interactive CLI**: The entire game runs in the CLI (Command Line Interface). Once started, you can keep playing by entering choices without restarting the program.
- **Use of External Modules**: 
  - cowsay for ASCII art
  - pyttsx3 for text-to-speech narration


### About the Project
RPG ASCII Battle was originally made for the CS50P course, but it grew into a fun way to experiment with core Python concepts such as classes, loops, randomness, and user input in a real game.

It’s not meant to be complex or polished, but rather a simple, replayable example of what you can build with fundamental Python skills.


### Future Updates
The game is finished in its current form, but it’s easy to imagine expanding it further. Possible improvements include more classes, additional abilities, deeper combat mechanics, or even a basic storyline.

