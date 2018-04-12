import random
import string
from words import Words

class Hangman:
    guesses = 8
    lettersGuessed = []
    guessed = ''
    
    def __init__(self, words):
        self.words = words
    
    def start(self):
        print 'Welcome to the game, Hangam!'
        print 'I am thinking of a word that is', len(self.words.secretWord), ' letters long.'
        print '-------------'
        
    def game(self, words):
        print 'You have ', self.guesses, 'guesses left.'

        self.getAvailable()
        
        letter = raw_input('Please guess a letter: ')
        if letter in self.lettersGuessed:
            self.getGuessed()

            print 'Oops! You have already guessed that letter: ', self.guesses
        elif letter in self.words.secretWord:
            self.lettersGuessed.append(letter)
            self.getGuessed()

            print 'Good Guess: ', self.guessed
        else:
            self.guesses -=1
            self.lettersGuessed.append(letter)
            self.getGuessed()
            
            print 'Oops! That letter is not in my word: ',  self.guessed
        print '------------'

    def getAvailable(self):
        available = self.words.getAvailableLetters()

        for letter in available:
            if letter in self.lettersGuessed:
                available = available.replace(letter, '')

        print 'Available letters', available
        return available

    def getGuessed(self):
        self.guessed = self.words.getGuessedWord()

        for letter in self.words.secretWord:
            if letter in self.lettersGuessed:
                self.guessed += letter
            else:
                self.guessed += '_ '
                
    def end(self):
        if self.words.isWordGuessed(self.words.secretWord, self.lettersGuessed) == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', self.words.secretWord, '.'
    