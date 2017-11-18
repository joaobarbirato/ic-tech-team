#!/bin/bash

fileName=$1
dataDir=$2
targetDir=$3

echo $fileName | python ../bin/main.py $dataDir $targetDir
        