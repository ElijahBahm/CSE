world_map = {
    'WESTHOUSE':{
        "NAME": 'WEST OF HOUSE',
        'DESCRIPTION': 'You are west of a small house.',
        'PATHS':{
            'NORTH': 'NORTHHOUSE',
            'SOUTH': "SOUTHHOUSE"
        }
    },
    'NORTHHOUSE':{
        "NAME": 'NORTH OF HOUSE',
        'DESCRIPTION': 'You are north of a small house.',
        'PATHS':{
            'WEST': "WESTHOUSE"
        }
    },
    'SOUTHHOUSE':{
        'NAME': 'SOUTH OF HOUSE',
        'DESCRIPTION': 'You are south of a small house.',
        'PATHS':{
            'WEST': "WESTHOUSE"
        }
    }
}

current_node = world_map['SOUTHHOUSE']
print(current_node['NAME'])
print(current_node['DESCRIPTION'])
