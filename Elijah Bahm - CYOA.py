import random

# Class Definitions
#     Items
#     Characters
#     Rooms
# Instantiation of classes
# Controller

# Item Classes

class Item(object):
    def __init__(self, name, description, use):
        self.name = name
        self.description = description
        self.use = use


class Healing(Item):
    def __init__(self, name, description, use, plus_health):
        super(Healing, self).__init__(name, description, use)
        self.plus_health = plus_health

        def add_health(self):
            if HealingKit or InstaHealth in inventory_real:
                self.plus_health += zero.health
            else:
                print ("You don't have any heals.")


class HealingKit(Healing):
    def __init__(self, name, description, plus_health, price):
        super(HealingKit, self).__init__(name, description, 'use', plus_health)
        self.price = price

        # def add_health(self):
        #     if HealingKit in inventory_real:
        #         print("You do those drugs and realize that this is a little weird. And also that you will be
        #               dependent on them very, very soon")
        #         self.plus_health += main_character.health


class InstaHealth(Healing):
    def __init__(self, name, description, plus_health):
        super(InstaHealth, self).__init__(name, description, 'use', plus_health)

        # def add_health(self):
        #     if InstaHealth in inventory_real:
        #         print("You drink up these weird colored vials, and think this is definitely going to cause some "
        #               "problems.")
        #         self.plus_health += main_character.health


class Shield(Item):
    def __init__(self, name, description, use, shield_health, ):
        super(Shield, self).__init__(name, description, use)
        self.shield_health = shield_health

        def shield_equals_heals(self):
            if Shield in inventory_real:
                self.shield_health += zero.health


class Piece(Item):
    def __init__(self, name, description, color):
        super(Piece, self).__init__(name, description, "use")
        self.color = color

        def glow(self):
            if Piece in inventory_real:
                print("Your bag, glows a bright pink.")


class Weapon(Item):
    def __init__(self, name, description, use, attack):
        super(Weapon, self).__init__(name, description, use)
        self.attack = attack


class Gun(Weapon):
    def __init__(self, name, description, attack, brand):
        super(Gun, self).__init__(name, description, "use", attack)
        self.brand = brand


class Shotgun(Gun):
    def __init__(self, name, description, attack, brand):
        super(Shotgun, self).__init__(name, description, attack, brand)

        def shot_gun(self):
            if self.name in shotguns:
                self.attack * 11


class SniperRifle(Gun):
    def __init__(self, name, description, attack, brand):
        super(SniperRifle, self).__init__(name, description, attack, brand)

        def snip_dip(self):
            if self.name in snip_dip:
                self.attack * 2


class RPG(Gun):
    def __init__(self, name, description, attack, brand):
        super(RPG, self).__init__(name, description, attack, brand)

        def helix_shot(self):
            if self.name in triplets:
                self.attack * 3


class Eridian(Gun):
    def __init__(self, name, description, attack, brand):
        super(Eridian, self).__init__(name, description, attack, brand)

        def eridian_snip(self):
            if self.name in eridian_sniper:
                self.attack * 2


class Pistol(Gun):
    def __init__(self, name, description, attack, brand):
        super(Pistol, self).__init__(name, description, attack, brand)

        def repeater(self):
            if self.name in repeater_type_pistol:
                self.attack * 5


class CombatRifle(Gun):
    def __init__(self, name, description, attack, brand):
        super(CombatRifle, self).__init__(name, description, attack, brand)

        def burst_rifle(self):
            if self.name in burst_combat_rifle:
                self.attack * 3


class SMG(Gun):
    def __init__(self, name, description, attack, brand):
        super(SMG, self).__init__(name, description, attack, brand)

        def fuego_rapido(self):
            if self.name in rapid_fire:
                self. attack * 10

# Character Classes

class Character(object):
    def __init__(self, name, description, inventory, health, money, attack, max_health):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.health = health
        self.money = money
        self.attack =attack
        self.max_health = max_health


    def equip(self, weapon):
        if weapon in inventory_real:
            input("Choose which weapon to equip.")
            if input in all_weapons and input in inventory_real:
                weapon.attack = self.attack

    # def pick_up(self, item):
    #     if item in current_node:
    #         inventory_real.append(current_node.item)

    def take_damage(self, amount):
        self.health -= amount

    def hit(self, target):
        target.take_damage(self.attack)
        print('%s attacks %s for %s' % (self.name, target.name, self.attack))
        if zero.health <= 0:
            print('You are very, very dead.')
            exit(0)
        if target.health <= 0:
            print('The %s is dead.' % target.name)
            self.money += target.money
            if target.health < 0:
                target.health = 0
                inventory_real.extend(target.inventory)

    def fight(self, enemy):
        try:
            if enemy == current_node.enemy:
                enemy.health = enemy.max_health
                while enemy.health != 0:
                    choice = random.choice([enemy, self])
                    if choice == self:
                        enemy.hit(self)
                        print("Nice shot!")
                        print(str(zero.health))
                        print(str(current_node.enemy.health))
                    elif choice == enemy:
                        self.hit(enemy)
                        print("Nice dodge.")

        except AttributeError:
            print("Stop swinging that thing around, you're DEFINITELY going to 'Accidentally' shoot somebody.")


class Enemy(Character):
    def __init__(self, name, description, inventory, health, money, attack, max_health):
        super(Enemy, self).__init__(name, description, inventory, health, money, attack, max_health)

# Room Class


class Room(object):
    def __init__(self, name, north, south, east, west, southwest, northwest, southeast, northeast, description, enemy):
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
        self.enemy = enemy

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]

# The useful lists


inventory_real = []
all_weapons = []
triplets = []
shotguns = []
snip_dip = []
repeater_type_pistol = []
rapid_fire = []
burst_combat_rifle = []
eridian_sniper = []

# Instantiation of Items

minor_kit = HealingKit("Minor Healing Kit", "Tiny Bottle of Dr. Zed's Horse Pills", 40, 10)
light_kit = HealingKit("Light Healing Kit", "Small Bottle of Dr. Zed's Bullet Salve", 80, 30)
kit = HealingKit("Mediocre Healing Kit", "Bottle of Dr. Zed's Body Spackle", 130, 60)
greater_kit = HealingKit("Greater Healing Kit", "Large Bottle of Dr. Zed's Bullet Salve", 170, 100)
super_kit = HealingKit("Super Healing Kit", "Giant Bottle of Dr. Zed's Horse Pills", 400, 300)

minor_insta = InstaHealth("Minor InstaHealth", "Vial of Red Fluid", 20)
light_insta = InstaHealth("Light InstaHealth", "Vial of Orange Fluid", 40)
insta = InstaHealth("InstaHealth", "Vial of Yellow Fluid", 60)
super_insta = InstaHealth("Super InstaHealth", "Vial of Pink Fluid", 120)

# The Pieces of the Key to the Vault

core = Piece("The Core", "This is probably the most important part of the key, it is very large and has many cracks in "
             "it. You believe that is just from how old it is, \n But in the back of your head you think it might be "
             "something much, much worse.", "The outside is a bluish, gray and it is radiating a pink glow.")

left_side = Piece("The Left Side of the Key", )

right_side = Piece("The Right Side of the Key", )
# Instantiation of Weapons
tks_wave = Shotgun("T.K's Wave", "Ride the Wave, Dude!", )
sledges_shotgun = Shotgun("Sledge's Shotgun", "The Legend Lives", )

golden_gun_galactic_destruction = Eridian("The Golden Gun Of Galactic Destruction", "What do you need as a "
                                          "description? It's right there, it's the name.", 10000, "Eridian")
# Instantiation of Enemies

skag_pup = Enemy("Skag pup", "A young dog like creature that can unhinge its jaw like a python.", [minor_insta], 200,
                 20, 10, 200)

skag = Enemy("Skag", "An adult, ugly dog like creature that has unhinging jaws.", [light_insta], 400, 25, 15, 400)

psycho = Enemy("Psycho", "An infuriated man who keeps screaming, 'I will skin you alive.'", [super_insta], 350, 40, 25,
               350)

badass_psycho = Enemy("Badass Psycho", "An even more infuriated man, who is much bigger than the other psychos and he "
                      "keeps screaming, 'When, I find you I'm gonna wear you as a hat'", [], 500, 55, 50, 500)

bandit = Enemy("Bandit", "", [insta, ], 250, 30, 15, 250)

badass_bandit = Enemy("Badass Bandit", "", [], 475, 50, 50, 475)

nine_toes = Enemy("Nine Toes", "", [], 350, 100, 75, 350)

sledge = Enemy("Sledge", "", [], 450, 150, 100, 450)

tk_baha = Enemy("T.K. Baha", "Your old mentor and friend, who was taken over by a brain slug and now it just sits there"
                " atop of his head.", [tks_wave], 500, 250, 150, 500)

swagger_souls = Enemy("Swagger Souls", "A high man in a knight helmet, who you somehow woke up and pissed off.", [],
                      1000, 500, 250, 1000)

leviathan = Enemy("The Guardian", "Better name The Leviathan.", ,)
# Instantiation of you

zero = Character("Zer0", "A ruthless assassin that has been enticed by the treasure here.", inventory_real, 180, 0, 20,
                 700)


loathing_des = input("What event made you loath someone or yourself the most? Please make this descriptive and "
                     "somewhat in depth.")

# Instantiation of the Rooms

town_square = Room("Town Square of Dust", "town_hall", None, "ride_station", "market", None, "public_restroom", None,
                   None, 'You are in a big open square in the center of this town. The big sign in front of you says '
                   '"WELCOME TO DUST".', None)

market = Room("The Market", None, None, "town_square", None, None, None, None, None, 'You are in what used to be a '
              'giant bazaar, now there is only one vendor open. \n His shop is only slightly nicer than the than the '
              'abandoned ones, mainly just less dusty.', None)

town_hall = Room("Town Hall", None, "town_square", None, "public_restroom", None, None, None, None, 'You are in a very'
                 ' long, dark, and tall building. It has a small display of the \n founding of the town and on of '
                 'something like a teleporter that needs a special key to use.', None)

public_restroom = Room("The One Public Restroom", None, None, "town_hall", None, None, None, "town_square", None, 'You '
                       'regret coming here, there is s#@!, c#@!, feces, whatever you want to call it, everywhere. \n '
                       'You have the slightest feeling that something useful will be here.', skag_pup)

ride_station = Room("Catch-A-Ride-Station", "badlands", "worlds_end", "death", "town_square", None, None, None, None,
                    'You are in a small area that is covered with a tin roof and has a terminal, that you \n assume '
                    'will either teleport you or spawn something for you.', bandit)

badlands = Room("The Badlands", None, "ride_station", "suffering", None, None, None, None, None, 'Again, you feel '
                'regret as soon as you come here, as soon as the eye can see there are \n just heads on bloody stakes '
                'and bodies strung up with chains every where else in the area. And, yet again, you feel that there '
                'will be something here.', badass_bandit)

suffering = Room("Suffering", None, "death", None, "badlands", None, None, None, None, 'You are in the remains of a '
                 'grand city and the last survivor from this city is an old man, \n who is very weak and malnourished, '
                 'he is only a couple feet away from you. You hold his life in the palm of your hand.', psycho)

death = Room("Death, The Town", "suffering", "sick", None, "ride_station", None, None, "damage_control", "loathing",
             'You are in the middle of what used to be a town, until sometime in the past day or past couple hours, \n '
             'it was burnt to the ground and all you can smell is burnt flesh. Oh, the irony here.', badass_psycho)

loathing = Room("Loathing", None, None, None, None, "death", None, None, None, 'You are in a place that has a projector'
                ' playing a bad time in your life, here it is. \n %s.' % loathing_des, tk_baha)

damage_control = Room("Damage Control", None, None, None, None, None, "death", None, None, 'You are in an open field '
                      'that has a hologram of what happened here, it is showing a big riot about something, which '
                      'caused the police to fight against the civilians.', sledge)

sick = Room("Sick", "death", None, None, "worlds_end", None, None, None, None, 'You are in a town of depressed, '
            'misunderstood people; to get what you need here you will have to understand what they go through.',
            swagger_souls)

worlds_end = Room("World's End, The Town", "ride_station", "regret", "sick", "hello", None, None, None, None, 'You are '
                  'in an aptly named town because sometime recently there was an earthquake that split the town almost'
                  ' in half and cut of their worlds from each other.', None)

regret = Room("Regret", "worlds_end", None, None, None, None, None, None, None, 'You are with the body of a man that '
              'deserves a Darwin Award, he somehow killed himself trying to cut down one of his own trees in his '
              'front yard.', nine_toes)

hello = Room("Hello", None, "novac", "worlds_end", None, None, None, None, None, "You meet someone here the first thing"
             " they say is the town's slogan 'We didn't want you to be forgot about, so we made our name something "
             "that is forever used.", None)

novac = Room("NoVac", "hello", None, None, None, None, None, None, None, 'You are in a place that was named again after'
             ' it was abandoned, you overhear this from a conversation a couple paces away from you, you see the "No '
             'Vacancy" sign that turned into the "NoVac" sign.', skag)

vault = Room("The Vault", None, None, None, None, None, None, None, None, '', leviathan)

current_node = town_square
directions = ['north', 'south', 'east', 'west', 'northwest', 'northeast', 'southeast', 'southwest']
short_directions = ['n', 's', 'e', 'w', 'nw', 'ne', 'se', 'sw']
the_king_of_commands = ['north', 'south', 'east', 'west', 'northwest', 'northeast', 'southeast', 'southwest', 'n', 's',
                        'e', 'w', 'nw', 'ne', 'se', 'sw', 'inventory', 'inv', 'help', 'kill self', 'seppuku', 'why do i'
                        ' have crippling depression?', 'yeet', 'fight', 'equip', 'all commands']

# The Controller

while True:
    print("If you need help navigating this game type 'help' to get the basics of the controls.")
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower().strip()

    if current_node == town_hall:
        if core and right_side and left_side in inventory_real:
            current_node = vault
            print("")

    if zero.health <= 0:
        exit(0)

    if command == 'quit':
        quit(0)

    if command == 'fight':
        print("<================}==========================================================================>>")
        print(current_node.enemy.name)
        print(current_node.enemy.descripton)
        zero.fight(current_node.enemy)
        # print(str(zero.health))
        # print(str(current_node.enemy.health))

    if command == 'seppuku':
        print("You turn your trusty sword against yourself because you feel like you have disrespected your sensei. \n "
              "You successfully disembowel yourself, but you are still alive, so you toss your sword to Claptrap who "
              "realizes what you are trying to do, and successfully beheads you, which finally kills this warrior. \n "
              "When this happens you wish you told Claptrap that he was finally useful.")
        zero.health = 0
        exit(0)

    if command == 'help':
        print("Type 'fight' to attack/fight. \n Type 'inventory' or 'inv' to look at what you have in your inventory. "
              "\n Type 'equip' to choose which weapon you are want to use. \n ")

    # if command == 'all commands':
    #     print(str(the_king_of_commands))

    elif command in short_directions:
        # Finds the command in shorts directions (index #)
        pos = short_directions.index(command)
        command = directions[pos]

    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print('Nope, Sorry. \n Try again.')
    elif command not in the_king_of_commands:
        print("Command Not Recognized. \n You might've messed up somewhere, type in 'all commands' and this will show "
              "the full list of useful commands.")
    print()
