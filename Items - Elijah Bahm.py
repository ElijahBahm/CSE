class Item(object):
    def __init__(self, name, description, use):
        self.name = name
        self.description = description
        self.use = use


class Healing(Item):
    def __init__(self, name, description, use, ):
        super(Healing, self).__init__(name, description, use)


class Shield(Item):
    def __init__(self, name, description, use, health, ):
        super(Shield, self).__init__(name, description, use)
        self.health = health
        self.


class Pieces(Item):
    def __init__(self, name, description, use, ):
        super(Pieces, self).__init__(name, description, use)
        self.
        self.


class Core(Pieces):
    def __init__(self):
        super(Core, self).__init__()


class Weapon(Item):
    def __init__(self, name, description, use, brand, ):
        super(Weapon, self).__init__(name, description, use)
        self.brand = brand
        self.


