class Room(******):
    def __init__(self, name, north, south, east, west, southwest, northwest, southeast, northeast, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.southwest = southwest
        self.northwest = northwest
        self.southeast = southeast
        self.northeast = northeast
        self.description = description

    def move(self, direction):
        global current_node         #global here somewhat bad practice
        current_node = globals()[getattr(self, direction)]


# north_house = Room("North of House", None)
# west_house = Room("West of House", "north_house")
town_square =