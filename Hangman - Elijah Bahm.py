import string
import random

"""
Outline of Hangman
1. Make a word bank - 10 items
2. Select a random item from the list 
3. Add user input to a list of letters_guessed
4. Build a list of letters to show, and display the string form
5. Create the Win condition
"""


Fav_Streamers = ["Fugglet", "Shroud", "HCJustin", "Box-Box", "ChocoTaco", "Cyanide Plays Games",
                 "Soviet Womble", "Achievement Hunter", "eMBeaR", "Oompaville", "Kugo"]
guess = "0"
guesses_left = 10
word = random.choice(Fav_Streamers)
hidden_word = ["%s" % word]
letters_guessed = []

while guesses_left > 0:
    guess = input("Choose a letter, to save your Friend.")
    if guess == letter in hidden_word:


    for letter in hidden_word:

