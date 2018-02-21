# Defining a class
class Cat(object):
    # Two underscores before and after / Means initialize
    def __init__(self, color, pattern):
        # Things that a cat has
        self.color = color
        self.pattern = pattern
        self.state = "happy"
        self.hungry = False

    # Things that a Cat can do
    def jump(self):
        self.state = "Scared"
        print("The cat jumps in the air")

    def play(self):
        self.state = "Happy"
        print("You play with the cat")


# Instantiating (creating) two cats
cute_cat = Cat("brown", "Spots")
cute_cat2 = Cat("grey", "Stripes")

# Getting Info about the cats
print(cute_cat.color)
print(cute_cat2.state)
print(cute_cat2.color)

cute_cat.jump()
print(cute_cat.state)
print(cute_cat2.state)

class Car(object):
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand
        self.engineOn = False

    def turn_on(self):
        if self.engineOn:
            print("Nothing Happens")
        else:
            print("The engine turns on")
            self.engineOn = True

    def move_forward(self):
        if self.engineOn:
            print("You move forward")
        else:
            print("Nothing Happens")

    def turn_off(self):
        if self.engineOn:
            self.engineOn = False
            print("You have turned off you're car")
        else:
            print("Nothing happens")

mycar = Car("red", "Ferrari")

mycar.turn_on()
mycar.move_forward()
mycar.turn_off()
