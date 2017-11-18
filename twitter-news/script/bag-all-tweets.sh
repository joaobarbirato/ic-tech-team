#!/bin/bash

# Author: João Gabriel Melo Barbirato
# Machine Learning Lab (MaLL UFSCar)
# Objective: script to run BoW on a colected (by twitter-crawler) twitter news dataset

# create parsed tweets
allFileNames=$(ls -p ../data | grep -v / )
totalFiles=$(ls -p ../data | grep -v / | wc -l)

# relative data and target directories at BoW's directory 
dataDir_BoW="./../../../data/parsed-tweets/"
targetDir_BoW="./../../../data/bags/"

# parsing tweets
cd ../bin
echo $allFileNames | python json-transform.py

# applying BoW on parsed tweets
for((i=0;i<totalFiles;i++))
do
	cd ../bin
	word=$(echo $allFileNames | python bag-manager.py $i)
	cd ../assets/bag-of-words/script
	sh run-me.sh $word $dataDir_BoW $targetDir_BoW
	cd ../..
done
#calling bag of words
