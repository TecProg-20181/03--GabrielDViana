import random
import string

class Words:
    wordlist = []
    
    def __init__(self, fileName):
        self.fileName = fileName
        self.loadWords()

    def loadWords(self):
        print "Loading word list from file..."
        
        inFile = open(self.fileName, 'r', 0)
        
        line = inFile.readline()
        
        self.wordlist = string.split(line)
        print "  ", len(self.wordlist), "words loaded."
        return random.choice(self.wordlist)


    def isWordGuessed(self, secretWord, lettersGuessed):
        secretLetters = []

    #    for letter in secretWord:
    #        if letter in secretLetters:
    #            secretLetters.append(letter)
    #        else:
    #            pass

        for letter in secretWord:
            if letter in lettersGuessed:
                pass
            else:
                return False

        return True

    def getGuessedWord(self):

        guessed = ''


        return guessed

    def getAvailableLetters(self):
        import string
        # 'abcdefghijklmnopqrstuvwxyz'
        available = string.ascii_lowercase


        return available