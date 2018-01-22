import string
import random

"""
Outline of Hangman
1. Make a word bank - 10 items
2. Select a random item from the list 
3. Hide the word (use *)
4. Reveal letters if they have been guessed
5. Create the Win condition
"""


Fav_Streamers = ["Fugglet", "Shroud", "HCJustin", "Box-Box", "ChocoTaco", "Cyanide Plays Games",
                 "Soviet Womble", "Achievement Hunter", "eMBeaR", "Oompaville", "Kugo"]
guess = "0"
guesses = 0
word = random.choice(Fav_Streamers)
letter = {"%s" % word}
letters_guessed = "a"

while guess != letter and guesses < 10:
    guess = input("Choose a letter, to save your Friend.")
