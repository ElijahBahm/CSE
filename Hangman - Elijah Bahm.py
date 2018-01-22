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


Word_Bank = ["Fugglet", "Shroud", "HCJustin", "Box-Box", "ChocoTaco", "Cyanide Plays Games",
             "Soviet Womble", "Achievement Hunter", "eMBeaR", "Oompaville", "Kugo"]
guess = "0"
word = random.r

while guess != word:
    