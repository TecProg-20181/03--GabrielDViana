import random
import string
from words import Words

class Hangman:
    guesses = 8
    lettersGuessed = []
    __guessed = ''
    
    def __init__(self, words):
        self.__words = words
    
    def start(self):
        print 'Welcome to the game, Hangam!'
        print 'I am thinking of a word that is', len(self.__words.secretWord), ' letters long.'
        print '-------------'
        
    def game(self, words):
        print 'You have ', self.guesses, 'guesses left.'

        self.__getAvailable()
        
        letter = raw_input('Please guess a letter: ')
        if letter in self.lettersGuessed:
            self.__getGuessed()

            print 'Oops! You have already guessed that letter: ', self.guesses
        elif letter in self.words.secretWord:
            self.lettersGuessed.append(letter)
            self.__getGuessed()

            print 'Good Guess: ', self.__guessed
        else:
            self.guesses -=1
            self.lettersGuessed.append(letter)
            self.__getGuessed()
            
            print 'Oops! That letter is not in my word: ',  self.__guessed
        print '------------'

    def __getAvailable(self):
        available = self.__words.getAvailableLetters()

        for letter in available:
            if letter in self.lettersGuessed:
                available = available.replace(letter, '')

        print 'Available letters', available
        return available

    def __getGuessed(self):
        self.__guessed = self.__words.getGuessedWord()

        for letter in self.__words.secretWord:
            if letter in self.lettersGuessed:
                self.__guessed += letter
            else:
                self.__guessed += '_ '
                
    def end(self):
        if self.__words.isWordGuessed(self.__words.secretWord, self.lettersGuessed) == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', self.__words.secretWord, '.'
    