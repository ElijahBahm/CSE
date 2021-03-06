'''
print("Hello World")

# Elijah Bahm

print(3+5)
print(5-3)
print(6/2)
print(5*3)
print(3**2)

print()
print("See if you can figure this out")
print(600 % 19)

# Variables
car_name = "Wiebe Mobile"
car_type = "Lamborghini Aventador"
car_cylinders = 12
car_mpg = 9000.1

# Inline Printing
print("My car is the %s." % car_name)
print("My car is the %s. It is a %s." % (car_name, car_type))

# Taking input
# name = input("What is your name?")
# print("Hello %s." % name)
# print(name)

# age = input("What is your age?")
# print("Goodbye is %s" % age)
# print("You belong in a museum!")

# Functions


def print_hw() :
    print("Hello World")


print_hw()


def say_hi(name):
    print("Hello %s." % name)
    print("I hope you have a good day")


say_hi("Sodapop")


def birthday(age):
    age += 1  # age = age + 1
    print(age)


say_hi("Sodapop")
print("Soda is 15. Next year:")
birthday(15)
#
#
def f(x):
    return x**5 + 4 * x ** 4 -17*x**2+4
#
#
print(f(3))
print(f(3)+f(5))
#
If statements
#
def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"
#
#
Loops
#
for num in range(5):
    print(num + 1)
#
for k in "Hello World":
    print(k)
#
response = ""
while response != "Hello":
    response = input("Say \"Hello\"")  # \ escape character
    print("Hello \nWorld") # \n = newline

import random
print(random.randint(0,6))  #imports should be at the top
#
#
Comparisons
print(1 == 1)   # Two equal signs to compare
print(1 != 2)   # One is not equal to 2
print(not False)   # This prints True
print(1 == 1 and 4 <= 5)
print(1 < 0 or 5 > 1)
#
#
Recasting
c = '1'  # string
print(c == 1)
print(int(c) == 1) # compares 2 ints
print(c == str(1)) # compares 2 strings
#
#
Lists
#
the_count = [1, 2, 3, 4, 5]
characters = ["Graves", "Dory", "Boots", "Dora", "Shrek", "Obi-wan", "Carl"]
print(characters[0])
print(characters[4])

print(len(characters))
len = length of list
#
Going through lists
for char in characters:
    print(char)

for num in the_count:
    print(num)
    print(num ** 2)

len(characters)
range(3)  # list of 0-2
range(len(characters))  # Makes a list of All Indices

for num in range(len(characters)):
    char = characters[num]
    print("The character at index %d is %s" % (num, char))   # %d is digit and %s is string

str1 = "Hello World!"
listOne = list(str1)
listOne[11] = '.'
print(listOne)
newStr = "".join(listOne)
print(newStr)
print(listOne[-1])
-index goes backwards

Add items from lists

characters.append("Ironman/by Black Sabbath")
print(characters)

characters.append("Fugglet")
print(characters)

Remove items from list

characters.remove("Carl")
print(characters)

characters.pop(4)
print(characters)
#
the string class
import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.digits)
print(string.punctuation)

strTwo = 'ThIs SeNtEncE iS UnUsUaL'
lowercase = strTwo.lower()
print(lowercase)
'''

''''''
# Dictionaries - make up a key: value pair
dictionary = {'name': 'Lance', 'age': 18, 'height': 6 * 12 + 2}

# Accessing from a dictionary: dictionary = no order
print(dictionary['name'])
print(dictionary['age'])
print(dictionary['height'])

# Adding to a dictionary
dictionary["eye colour"] = "bleu"
dictionary["paper towels"] = True
print(dictionary)

'''
large_dictionary = {
    "California": "CA",
    "Michigan": "MI",
    "Florida": "FL"
}
print(large_dictionary["Florida"])

larger_dictionary = {
    "California": [
        'Fresno',
        'Sacremento',
        'Los Angeles',
    ],
    "Michigan": [
        'Detroit',
        "Kalamazoo",
        "Flint",
    ],
    "Florida": [
        "Miami",
        "Fort Lauderdale"
    ],
    "Washington": [
        "Spokane"
        "Seattle"
        "Tacoma"
        "Spokane"
    ]
}

print(larger_dictionary['Michigan'])
print(larger_dictionary["Michigan"][0])
# print(larger_dictionary["Washington"[3]])


xxl_dictionary = {
    "CA": {
        'Name': "California",
        "Population": 39250000,
        "Border ST": [
        'Oregon',
        "Nevada",
        "Arizona"
        ]
    },
    "MI": {
        "Name": "Michigan",
        "Population": 9928000,
        "Border ST": [
            'Wisconsin',
            'Ohio',
            'Indiana'
        ]
    },
    "FL": {
        "Name": "Florida",
        "Population": 20610000,
        "Border ST": [
            'Georgia',
            'Alabama'
        ]
    }
}


# print(xxl_dictionary["MI"]["Border ST"][2])
print(xxl_dictionary["MI"]["Border ST"][1])
'''
