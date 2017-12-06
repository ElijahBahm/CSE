import random
# Elijah Bahm

number = (random.randint(1, 50))
print("Guess a number 1-50.")
guess = "0"
guess_amount = 0


while int(guess) != number:
    guess = input("What is your guess?")
    if guess == str(number):
        print("Correct.")
    elif (int(guess) >= number):
        print("Lower.")
    elif (int(guess) <= number):
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