world_map = {
    'TOWNSQUARE': {
        'NAME': 'TOWN SQUARE OF DUST',
        'DESCRIPTION': 'You are in a big open square in the center of this town. The big sign in front of you '
                       'says WELCOME TO DUST',
        'PATHS': {
            'NORTH': 'TOWNHALL',
            'WEST': 'MARKET'
        }
    },
    'MARKET': {
        'NAME': 'THE MARKET',
        'DESCRIPTION': 'You are in what used to be a giant bazaar, now there is only one vendor open. \n His shop'
                       ' is only slightly nicer than the than the abandoned ones, mainly just less dusty.',
        'PATHS': {
            'EAST': 'TOWNSQUARE'
        }
    },
    'TOWNHALL': {
        'NAME': 'TOWN HALL',
        'DESCRIPTION': 'You are in a very long, dark, and tall building. It has a small display of the \n '
                       'founding of the town and on of something like a teleporter that needs a special key to use.',
        'PATHS': {
            'WEST': "PUBLICRESTROOM",
            'SOUTH': 'TOWNSQUARE'
        }
    },
    'PUBLICRESTROOM': {
        'NAME': 'THE ONE PUBLIC RESTROOM',
        'DESCRIPTION': '',
        'PATHS': {
            'SOUTHEAST': 'TOWNSQUARE',
            'EAST': 'TOWNHALL'
        }
    },
    'RIDESTATION': {
        'NAME': 'CATCH-A-RIDE STATION',
        'DESCRIPTION': '',
        'PATHS': {
            'NORTH': 'BADLANDS',
            'WEST': 'TOWNSQUARE',
            'SOUTH': 'WORLDS_END',
            'EAST': 'DEATH'
        }
    },
    'BADLANDS': {
        'NAME': 'THE BADLANDS',
        'DESCRIPTION': '',
        'PATHS': {
            'SOUTH': 'RIDESTATION',
            'EAST': 'SUFFERING'
        }
    },
    'SUFFERING': {
        'NAME': 'SUFFERING',
        'DESCRIPTION': '',
        'PATHS': {
            'SOUTH': 'DEATH',
            'WEST': 'BADLANDS'
        }
    },
    'DEATH': {
        'NAME': 'DEATH, "THE TOWN"',
        'DESCRIPTION': '',
        'PATHS': {
            'SOUTH': 'SICK',
            'WEST': 'RIDESTATION',
            'NORTH': 'SUFFERING',
            'SOUTHEAST': 'DAMAGECONTROL',
            'NORTHEAST': 'LOATHING'
        }
    },
    'LOATHING': {
        'NAME': 'LOATHING',
        'DESCRIPTION': '',
        'PATHS': {
            'SOUTHWEST': 'DEATH'
        }
    },
    'DAMAGECONTROL': {
        'NAME': 'DAMAGE CONTROL',
        'DESCRIPTION': '',
        'PATHS': {
            'NORTHWEST': 'DEATH'
        }
    },
    '': {
        'NAME': '',
        'DESCRIPTION': '',
        'PATHS': {
            'SOUTH': '',
            'WEST': ''
        }
    },
}

current_node = world_map['TOWNSQUARE']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'NORTHWEST', 'NORTHEAST', 'SOUTHEAST', 'SOUTHWEST']

while True:
    print(current_node["NAME"])
    print(current_node["DESCRIPTION"])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print('You cannot got that way')
    else:
        print('Command Not Recognized.')
    print()
