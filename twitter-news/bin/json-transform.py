# Author: João Gabriel Melo Barbirato
# Machine Learning Lab (MaLL UFSCar)
# Objective: parse tweets collected by twitter api into a raw txt file

import json, sys
sys.path.append('./../data')

txtFileNames = input('').split(' ')

# delete 2 first lines (auth msgs)
# this will result into a file which contains lots of tweets in json lines 
for name in txtFileNames:
	txtFile = open("./../data/"+name, 'rt')
	lines = txtFile.readlines()
	txtFile.close()
	
	txtFile = open("./../data/no-header/"+"no-header-"+name, 'wt')
	txtFile.writelines(lines[2:-1])
	txtFile.close()

# convert every json to a raw txt file
for name in txtFileNames:	
	txtFile = open("./../data/no-header/"+"no-header-"+name, 'rt')
	rawTweets = txtFile.readlines()
	txtFile.close()
	
	txtFile = open("./../data/parsed-tweets/"+"parsed-"+name, 'wt')
	for tweet in rawTweets:
		txtFile.write(json.loads(tweet)["status"]) # write tweet content only
		txtFile.write(" | ")
	
	txtFile.close()