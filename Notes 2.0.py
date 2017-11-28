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