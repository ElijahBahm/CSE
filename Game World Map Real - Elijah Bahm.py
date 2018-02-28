loathing_des = input("What event made you loath someone or yourself the most? Please make this descriptive and "
                     "somewhat in depth.")

world_map = {
    'TOWNSQUARE': {
        'NAME': 'TOWN SQUARE OF DUST',
        'DESCRIPTION': 'YOU ARE IN A BIG OPEN SQUARE IN THE CENTER OF THIS TOWN. THE BIG SIGN IN FRONT OF YOU '
                       'SAYS "WELCOME TO DUST".',
        'PATHS': {
            'NORTH': 'TOWNHALL',
            'WEST': 'MARKET',
            'NORTHWEST': 'PUBLICRESTROOM',
            'EAST': 'RIDESTATION'
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
        'DESCRIPTION': 'You regret coming here, there is s#@!, c#@!, feces, whatever you want to call it, everywhere.'
                       '\n You have the slightest feeling that something useful will be here.',
        'PATHS': {
            'SOUTHEAST': 'TOWNSQUARE',
            'EAST': 'TOWNHALL'
        }
    },
    'RIDESTATION': {
        'NAME': 'CATCH-A-RIDE STATION',
        'DESCRIPTION': 'You are in a small area that is covered with a tin roof and has a terminal, that you \n '
                       'assume will either teleport you or spawn something for you.',
        'PATHS': {
            'NORTH': 'BADLANDS',
            'WEST': 'TOWNSQUARE',
            'SOUTH': 'WORLDS_END',
            'EAST': 'DEATH'
        }
    },
    'BADLANDS': {
        'NAME': 'THE BADLANDS',
        'DESCRIPTION': 'Again, you feel regret as soon as you come here, as soon as the eye can see there are \n '
                       'just heads on bloody stakes and bodies strung up with chains every where else in the area.'
                       '\n And, yet again, you feel that there will be something here.',
        'PATHS': {
            'SOUTH': 'RIDESTATION',
            'EAST': 'SUFFERING'
        }
    },
    'SUFFERING': {
        'NAME': 'SUFFERING',
        'DESCRIPTION': 'You are in the remains of a grand city and the last survivor from this city is an old man, \n '
                       'who is very weak and malnourished, he is only a couple feet away from you. \n '
                       'You hold his life in the palm of your hand.',
        'PATHS': {
            'SOUTH': 'DEATH',
            'WEST': 'BADLANDS'
        }
    },
    'DEATH': {
        'NAME': 'DEATH, "THE TOWN"',
        'DESCRIPTION': 'You are in the middle of what used to be a town, until sometime in the past day or past '
                       'couple hours, \n it was burnt to the ground and all you can smell is burnt flesh. '
                       'Oh, the irony here.',
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
        'DESCRIPTION': 'You are in a place that has a projector playing a bad time in your life, here it is %s.'
                       % loathing_des,       # This will be input taken at the start.
        'PATHS': {
            'SOUTHWEST': 'DEATH'
        }
    },
    'DAMAGECONTROL': {
        'NAME': 'DAMAGE CONTROL',
        'DESCRIPTION': 'You are in an open field that has a hologram of what happened here, it is showing a big riot '
                       'about something, which caused the police to fight against the civilians.',
        'PATHS': {
            'NORTHWEST': 'DEATH'
        }
    },
    'SICK': {
        'NAME': 'SICK',
        'DESCRIPTION': 'You are in a town of depressed, misunderstood people; to get what you need here you will '
                       'have to understand what they go through.',
        'PATHS': {
            'NORTH': 'DEATH',
            'WEST': 'WORLDSEND'
        }
    },
    'WORLDSEND': {
        'NAME': "WORLD'S END, THE TOWN",
        'DESCRIPTION': 'You are in an aptly named town because sometime recently there was an earthquake that split '
                       'the town almost in half and cut of their worlds from each other.',
        'PATHS': {
            'SOUTH': 'REGRET',
            'WEST': 'HELLO',
            'NORTH': 'RIDESTATION',
            'EAST': 'SICK'
        }
    },
    'REGRET': {
        'NAME': 'REGRET',
        'DESCRIPTION': 'You are with the body of a man that deserves a Darwin Award, he somehow killed himself trying '
                       'to cut down one of his own trees in his front yard.',
        'PATHS': {
            'NORTH': 'WORLDSEND'
        }
    },
    'HELLO': {
        'NAME': 'HELLO',
        'DESCRIPTION': "You meet someone here the first thing they say is the town's slogan 'We didn't want you to be "
                       "forgot about, so we made our name something that is forever used.",
        'PATHS': {
            'SOUTH': 'NOVAC',
            'EAST': 'WORLDSEND'
        }
    },
    'NOVAC': {
        'NAME': 'NOVAC',
        'DESCRIPTION': 'You are in a place that was named again after it was abandoned, you overhear this from a '
                       'conversation a couple paces away from you, you see the "No Vacancy" sign that turned into the '
                       '"NoVac" sign.',
        'PATHS': {
            'NORTH': 'HELLO'
        }
    }
}
()

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
            print('Nope, Sorry.')
    else:
        print('Command Not Recognized.')
    print()
