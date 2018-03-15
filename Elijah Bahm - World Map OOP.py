loathing_des = input("What event made you loath someone or yourself the most? Please make this descriptive and "
                     "somewhat in depth.")

class Room(object):
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
public_restroom = Room("The One Public Restroom", None, None, "town_hall", None, None, None, "town_square", None, 'You '
                       'regret coming here, there is s#@!, c#@!, feces, whatever you want to call it, everywhere. \n You have the slightest feeling that something useful will be here.')
ride_station = Room("Catch-A-Ride-Station", "badlands", "worlds_end", "death", "town_square", None, None, None, None,
                    'You are in a small area that is covered with a tin roof and has a terminal, that you \n assume will either teleport you or spawn something for you.')
badlands = Room("The Badlands", None, "ride_station", "suffering", None, None, None, None, None, 'Again, you feel '
                'regret as soon as you come here, as soon as the eye can see there are \n just heads on bloody stakes '
                'and bodies strung up with chains every where else in the area. And, yet again, you feel that there will be something here.')
suffering = Room("Suffering", None, "death", None, "badlands", None, None, None, None, 'You are in the remains of a '
                 'grand city and the last survivor from this city is an old man, \n who is very weak and malnourished, '
                 'he is only a couple feet away from you. You hold his life in the palm of your hand.')
death = Room("Death, The Town", "suffering", "sick", None, "ride_station", None, None, "damage_control", "loathing",
             'You are in the middle of what used to be a town, until sometime in the past day or past couple hours, \n '
             'it was burnt to the ground and all you can smell is burnt flesh. Oh, the irony here.')
loathing = Room("Loathing", None, None, None, None, "death", None, None, None, 'You are in a place that has a projector '
                'playing a bad time in your life, here it is %s.' % loathing_des)
damage_control = Room("Damage Control", None, None, None, None, None, "death", None, None, 'You are in an open field '
                      'that has a hologram of what happened here, it is showing a big riot about something, which caused the police to fight against the civilians.')
sick = Room("Sick", "death", None, None, "worlds_end", None, None, None, None, 'You are in a town of depressed, '
            'misunderstood people; to get what you need here you will have to understand what they go through.')
worlds_end = Room("World's End, The Town", "ride_station", "regret", "sick", "hello", None, None, None, None, 'You are '
                  'in an aptly named town because sometime recently there was an earthquake that split the town almost in half and cut of their worlds from each other.')
regret = Room("Regret", "worlds_end", None, None, None, None, None, None, None, 'You are with the body of a man that '
              'deserves a Darwin Award, he somehow killed himself trying to cut down one of his own trees in his front yard.')
hello = Room("Hello", None, "novac", "worlds_end", None, None, None, None, None, "You meet someone here the first thing "
             "they say is the town's slogan 'We didn't want you to be forgot about, so we made our name something that is forever used.")
novac = Room("NoVac", "hello", None, None, None, None, None, None, None, 'You are in a place that was named again after '
             'it was abandoned, you overhear this from a conversation a couple paces away from you, you see the "No Vacancy" sign that turned into the "NoVac" sign.')
current_node = town_square
directions = ['north', 'south', 'east', 'west', 'northwest', 'northeast', 'southeast', 'southwest']
short_directions = ['n', 's', 'e', 'w', 'nw', 'ne', 'se', 'sw']


while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        # Finds the command in shorts directions (index #)
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print('Nope, Sorry.')
    else:
        print('Command Not Recognized.')
    print()
