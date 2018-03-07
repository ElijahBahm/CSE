# Character Class notes : Name, Description, Dialogue?, Inventory, Interact, Move?, Look, Item, Fight, Health, TakeDamage, Stats
class Character(object):
    def __init__(self, name, description, inventory, weaponry, health):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.weaponry = weaponry
        self.health = health
        self.state = "Bored."
        self.dialogue = "Hello. Do I Know You?"

    def meet(self):
        self.state = "Puzzled."
        print("How did you get here?")

    def