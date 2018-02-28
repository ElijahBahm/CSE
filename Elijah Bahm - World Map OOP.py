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
town_square = Room("Town Square of Dust", "town_hall", None, "ride_station", "market", None, "public_restroom", None,
                   None, 'You are in a big open square in the center of this town. The big sign in front of you says "WELCOME TO DUST".')
market = Room("The Market", None, None, "town_square", None, None, None, None, None, 'You are in what used to be a giant'
              ' bazaar, now there is only one vendor open. \n His shop is only slightly nicer than the than the abandoned ones, mainly just less dusty.')
town_hall = Room("Town Hall", None, "town_square", None, "public_restroom", None, None, None, None, 'You are in a very '
                 'long, dark, and tall building. It has a small display of the \n founding of the town and on of something like a teleporter that needs a special key to use.')
