import pytest
from project import Player, Adventurer, Warrior, Mage, Archer, Monster

def test_player_initialization():
    player = Player("Adventurer")  # Assuming 'Adventurer' is a valid class for Player
    assert 500 <= player._health <= 1500
    assert 50 <= player._power <= 150
    assert 25 <= player._defense <= 75
    assert 25 <= player._accuracy <= 75
    assert 25 <= player._agility <= 75

def test_adventurer_initialization():
    adventurer = Adventurer("Adventurer")
    assert adventurer._skill1 == "Swift Strike"
    assert adventurer._skill2 == "Focus Strike"  # Assuming this is the correct skill name

def test_warrior_initialization():
    warrior = Warrior("Warrior")
    assert warrior._skill1 == "Heavy Slash"
    assert warrior._skill2 == "Shield Bash"

def test_mage_initialization():
    mage = Mage("Mage")
    assert mage._skill1 == "Fireball"
    assert mage._skill2 == "Blizzard"

def test_archer_initialization():
    archer = Archer("Archer")
    assert archer._skill1 == "Quick Shot"
    assert archer._skill2 == "Arrow Rain"

def test_monster_initialization():
    monster = Monster()
    assert 500 <= monster.health <= 1500
    assert 0 <= monster.defense <= 40