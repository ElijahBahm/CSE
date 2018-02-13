world_map = {
    'TOWNSQUARE': {
        'NAME': 'TOWN SQUARE OF DUST',
        'DESCRIPTION': 'You are in a big open square in the center of this town. The big sign in front of you '
                       'says WELCOME TO DUST',
        'PATHS': {
            'NORTH': 'NORTHHOUSE',
            'SOUTH': 'SOUTHHOUSE'
        }
    },
    'MARKET': {
        'NAME': 'THE MARKET',
        'DESCRIPTION': 'You are in what used to be a giant bazaar, now there is only one vendor open. /n His shop'
                       ' is only slightly nicer than the than the abandoned ones, mainly just less dusty.',
        'PATHS': {
            'WEST': 'WESTHOUSE'
        }
    },
    'TOWNHALL': {
        'NAME': 'TOWN HALL',
        'DESCRIPTION': 'You are in a very long, dark, and tall building. It has a small display of the '
                       'founding of the town and on of something like a teleporter that needs a special key to use.',
        'PATHS': {
            'WEST': "WESTHOUSE"
        }
    },
    'PUBLICRESTROOM': {
        'NAME': 'THE ONE PUBLIC RESTROOM',
        'DESCRIPTION': ''



    }
}


print(world_map['MARKET']['DESCRIPTION'])