# Character Class notes : Name, Description, Dialogue?, Inventory, Interact, Move?, Look, Item, Fight, Health,
# TakeDamage, Stats
import random


class Character(object):
    def __init__(self, name, description, inventory, weaponry, health, attack):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.weaponry = weaponry
        self.health = health
        self.state = "Afraid."
        self.attack = attack
        # self.dialogue = "Hello."

    def meet(self):
        self.state = "Puzzled."
        # self.dialogue = "Where are we?"

    def befriend(self):
        self.state = "Happy."

    def attack(self):
        self.state = "Afraid."

    def defend(self):
        if self.attack >= 5:
            self.health - (self.attack - 4)


# command =
# attack_commands = ["attack", "kill", "fight"]

main_character = Character("Zer0", "A ruthless assassin that has been enticed by the treasure here.", "Very Small "
                           "Backpack", "Sword", 15, random.randint(1, 9))
