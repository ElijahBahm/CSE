# Character Class notes : Name, Description, Dialogue?, Inventory, Interact, Move?, Look, Item, Fight, Health, TakeDamage, Stats
import random
class Character(object):
    def __init__(self, name, description, inventory, weaponry, health):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.weaponry = weaponry
        self.health = health
        self.state = "Afraid."
        self.damage = random.randint(1, 9)
        # self.dialogue = "Hello."

    def meet(self):
        self.state = "Puzzled."
        # self.dialogue = "Where are we?"

    def befriend(self):
        self.state = "Happy."

    def attack(self):
        self.state = "Afraid."


main_charcter = (input("What is your name?"),"l", input("What do you want to carry your items?"), )