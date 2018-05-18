import random
import string
from words import Words
from hangman import Hangman


def main():
    __WORDLIST_FILENAME = "palavras.txt"
    words = Words(__WORDLIST_FILENAME)
    hangman = Hangman(words)
    
    hangman.start()

    while  words.isWordGuessed(words.secretWord, hangman.lettersGuessed) == False and hangman.guesses >0:
        hangman.game(words)
    else:
        hangman.end()

main()
