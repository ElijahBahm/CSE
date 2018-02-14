world_map = {
    'WESTHOUSE': {
        "NAME": 'WEST OF HOUSE',
        'DESCRIPTION': 'You are west of a small house.',
        'PATHS': {
            'NORTH': 'NORTHHOUSE',
            'SOUTH': "SOUTHHOUSE"
        }
    },
    'NORTHHOUSE': {
        "NAME": 'NORTH OF HOUSE',
        'DESCRIPTION': 'You are north of a small house.',
        'PATHS': {
            'WEST': "WESTHOUSE"
        }
    },
    'SOUTHHOUSE': {
        'NAME': 'SOUTH OF HOUSE',
        'DESCRIPTION': 'You are south of a small house.',
        'PATHS': {
            'WEST': "WESTHOUSE"
        }
    }
}

current_node = world_map['SOUTHHOUSE']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']

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
