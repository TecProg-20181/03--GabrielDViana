import random
import string
from words import Words
from hangman import Hangman
import gc
import sys

def main():
    __WORDLIST_FILENAME = "palavras.txt"
    words = Words(__WORDLIST_FILENAME)
    hangman = Hangman(words)
    
    hangman.start()

    while  words.isWordGuessed(words.secretWord, hangman.lettersGuessed) == False and hangman.guesses >0:
        hangman.game()
    else:
        hangman.end()
        gc.collect()
        sys.exit()

main()
