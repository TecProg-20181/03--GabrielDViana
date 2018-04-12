import random
import string

class Words:
    wordlist = []
    
    def __init__(self, fileName):
        self.fileName = fileName
        self.loadWords()
        self.secretWord = self.loadWords().lower()

    def loadWords(self):
        print "Loading word list from file..."
        
        inFile = open(self.fileName, 'r', 0)        
        line = inFile.readline()
        
        self.wordlist = string.split(line)
        print "  ", len(self.wordlist), "words loaded."
        
        return random.choice(self.wordlist)


    def isWordGuessed(self, secretWord, lettersGuessed):
        for letter in secretWord:
            if letter in lettersGuessed:
                pass
            else:
                return False
        return True

    def getGuessedWord(self):
        return ''

    def getAvailableLetters(self):
        return string.ascii_lowercase