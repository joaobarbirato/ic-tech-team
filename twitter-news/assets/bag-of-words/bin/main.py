# -*- coding: utf-8 -*-
import sys
sys.path.append('./../source')

from NoStopWords import NoStopWords
import Bag

fileName = input()
dataDir = sys.argv[1]
targetDir = sys.argv[2]

print(fileName)

bag = Bag.Bag()

rawText = open(dataDir+"parsed-"+fileName, "rt")

words = rawText.read()
words = words.lower()

words = NoStopWords(words)
words = words.split(' ')

for w in words:
    if(bag.isInTheBag(w)):
        bag.setTimesWord(w)
    else:
        bag.addWord(w)

bag.archiveDictAsJSON(targetDir+"bag-"+fileName)
