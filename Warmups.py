# name = input("What is your first name?")
# lastname = input("What is your last name?")
# print("Hello %s." % lastname % name)

def reverse_order(first_name, last_name):
    print("%s %s" % (last_name, first_name))
    print("" + last_name + "" +first_name)

def reverse_order():
    first_name = input("What is your first name?")
    last_name = input("What is your last name?")
    print("%s %s" % (last_name, first_name))

"""Warmup #2
Write a function called "happy_bday"
that prints
the Happy Birthday Song 

It must take one parameter called "name"
"""


def happy_bday(name):
    print("Happy Birthday to you,")
    print("Happy Birthday to you,")
    print("Happy Birthday dear %s" % name)
    print("Happy Birthday to you!")


""" Write a function called add_py
that takes one parameter caled "name"
and prints out name.py
example:
add_py("I_ate_some") == "I_ate_some.py"
"""


def add_py(name):
    name = input("Name please.")
    print("%s.py" % name)
    print(name + ".py")