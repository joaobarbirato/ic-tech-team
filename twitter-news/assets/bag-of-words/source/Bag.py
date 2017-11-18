import json

class Bag(object):
    #dictionary/JSON goes here
    def __init__(self):
        self.__dictionary = {}

    #checks if a word is in the bag
    def isInTheBag(self, key):
        if(key in self.__dictionary):
            return True
        return False

    #add a new word to database
    def addWord(self, key):
        self.__dictionary[key] = 1

    #+1 on existing word counter
    def setTimesWord(self, key):
        self.__dictionary[key] = self.__dictionary[key] + 1

    #puts JSON into a file
    def archiveDictAsJSON(self, fileName):
        self.__js = json.dumps(self.__dictionary)
        self.__logicFile = open(fileName, "wt")
        json.dump(self.__js, self.__logicFile)
        self.__logicFile.close()

    def printDictionary(self):
        print(self.__dictionary)

    #destructor
    def __del__(self):
        pass
