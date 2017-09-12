import json

class Bag(object):
    #dictionary/JSON goes here
    def __init__(self):
        self.dictionary = {}
        pass

    #checks if a word is in the bag
    def isInTheBag(self, string):
        pass

    #add a new word to database
    def addWord(self, string):

        pass

    #+1 on existing word counter
    def setTimesWord(self, string):
        pass

    #puts JSON into a file
    def archiveJSON(self):
        self.js = json.loads(dictionary)
        pass


    def __del__(self):
        pass
