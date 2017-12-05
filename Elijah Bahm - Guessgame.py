import random
# Elijah Bahm

print(random.randint(1, 50))
number = (random.randint(1, 50))
print("Guess a number 1-50.")
guess = input("What is your guess?")
if (int(guess) == number):
    print("Correct.")
if (int(guess) > number):
    print("Lower.")
if (int(guess) < number):
    print("Higher.")



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