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