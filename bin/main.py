import sys
sys.path.append('./../source')

#call everything and do stuff
import Bag

bag = Bag.Bag()

rawText = open("./../data/raw-text2.txt", "rt")
words = rawText.read().split(' ')

for w in words:
    if(bag.isInTheBag(w)):
        bag.setTimesWord(w)
    else:
        bag.addWord(w)

bag.archiveDictAsJSON("./../data/raw-text-2-json.txt")
