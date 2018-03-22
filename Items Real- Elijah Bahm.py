class Item(object):
    def __init__(self, name, description, use):
        self.name = name
        self.description = description
        self.use = use


class Healing(Item):
    def __init__(self, name, description, use, ):
        super(Healing, self).__init__(name, description, use)
        self.


class Healing_Kit(Healing):
    def __init__(self, name, description, use, ):
        super(Healing_Kit, self).__init__(name, description, use, )
        self.


class InstaHealth(Healing):
    def __init__(self, name, description, use, ):
        super(InstaHealth, self).__init__(name, description, use, )
        self.


class Shield(Item):
    def __init__(self, name, description, use, health, ):
        super(Shield, self).__init__(name, description, use)
        self.health = health
        self.


class Pieces(Item):
    def __init__(self, name, description, use, color, ):
        super(Pieces, self).__init__(name, description, use)
        self.color = color
        self.


class Core(Pieces):
    def __init__(self, name, description, use, color, ):
        super(Core, self).__init__(name, description, use, color)
        self.


class Weapon(Item):
    def __init__(self, name, description, use, brand, attack):
        super(Weapon, self).__init__(name, description, use)
        self.brand = brand
        self.attack = attack

