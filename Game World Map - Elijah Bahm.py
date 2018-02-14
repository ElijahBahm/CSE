world_map = {
    'TOWNSQUARE': {
        'NAME': 'TOWN SQUARE OF DUST',
        'DESCRIPTION': 'You are in a big open square in the center of this town. The big sign in front of you '
                       'says WELCOME TO DUST',
        'PATHS': {
            'NORTH': 'TOWNHALL',
            'WEST': 'MARKET'
            ''
        }
    },
    'MARKET': {
        'NAME': 'THE MARKET',
        'DESCRIPTION': 'You are in what used to be a giant bazaar, now there is only one vendor open. \n His shop'
                       ' is only slightly nicer than the than the abandoned ones, mainly just less dusty.',
        'PATHS': {
            'WEST': 'WESTHOUSE'
        }
    },
    'TOWNHALL': {
        'NAME': 'TOWN HALL',
        'DESCRIPTION': 'You are in a very long, dark, and tall building. It has a small display of the \n '
                       'founding of the town and on of something like a teleporter that needs a special key to use.',
        'PATHS': {
            'WEST': "WESTHOUSE"
        }
    },
    'PUBLICRESTROOM': {
        'NAME': 'THE ONE PUBLIC RESTROOM',
        'DESCRIPTION': '',
        'PATHS': {
            'SOUTHEAST': 'TOWNSQUARE'
        }
    }
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
