import sys
sys.path.append('../source')

#call everything and do stuff
import Bag

bag = Bag.Bag()

rawText = open("../data/raw-text.txt", "rt")
words = rawText.read().split(' ')

for w in words:
    if(w in bag.dictionary):
        bag.setTimesWord(w)
    else:
        bag.addWord(w)
