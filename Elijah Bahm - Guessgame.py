import random
# Elijah Bahm

# Initializing Variables
number = (random.randint(1, 50))
print("Guess a number 1-50.")
guess = "0"
guesses = 0

# Describes one turn. The while loop is the Game Controller.
while int(guess) != number and guesses < 5:
    guess = input("What is your guess?")
    if guess == str(number):
        print("Correct.")
    elif (int(guess) >= number):
        print("Lower.")
        guesses += 1
    elif (int(guess) <= number):
        print("Higher.")
        guesses += 1
if guesses >= 5:
    print("Get le f@#$ed.")


# print(int(c) == 1)
# response = ""
# while response != "Hello":
#     response = input("Say \"Hello\"")  # \ escape character
#     print("Hello \nWorld") # \n = newline
# Generate #
# Get a #(input) from user
# Compare # to input
# Add higher or lower
# Add guesses

# Make variable for guesses