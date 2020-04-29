#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Yiran Shao"
__email__ = "yshao242@uwo.ca"
__status__ = "Prototype"

##
# This program takes the name of the tweets
# file and the keywords file to compute the
# happiness score of each timezone, then it
# gives out a list containing 3 tuples of
# three values, average, count of keywords tweets
# and count of tweets
#

import string

# Values of the points used to determine the region of each tweet
p1 = [49.189787, -67.444574]
p2 = [24.660845, -67.444574]
p3 = [49.189787, -87.518395]
p4 = [24.660845, -87.518395]
p5 = [49.189787, -101.998892]
p6 = [24.660845, -101.998892]
p7 = [49.189787, -115.236428]
p8 = [24.660845, -115.236428]
p9 = [49.189787, -125.242264]
p10 = [24.660845,-125.242264]

def remove_punctuation(sentence):
    # Function that removes all the punctuation from the beginning
    # or end of the words in a sentence
    newSentence = []
    for word in sentence:
        word = word.strip(string.punctuation)
        newSentence.append(word)
    return newSentence


def area_range (p1,p2,p3,p4):
    # Function that determines the lower and upper limits of latitude
    # and longitude of a geographical boundary
    lat = [p1[0],p2[0],p3[0],p4[0]]
    long = [p1[1],p2[1],p3[1],p4[1]]
    minLat = float(min(lat))
    maxLat = float(max(lat))
    minLong = float(min(long))
    maxLong = float(max(long))
    return[[minLat, maxLat],[minLong, maxLong]]


def return_area(lat,long):
    # Function that returns the timezone of a tweet
    eastern = area_range(p1,p2,p3,p4)
    central = area_range(p3,p4,p5,p6)
    mountain = area_range(p5,p6,p7,p8)
    pacific = area_range(p7,p8,p9,p10)
    if eastern[0][0] < lat < eastern[0][1] and eastern[1][0] < long < eastern[1][1]:
        area = "eastern"
    elif central[0][0] < lat < central[0][1] and central[1][0] < long < central[1][1]:
        area = "central"
    elif mountain[0][0] < lat < mountain[0][1] and mountain[1][0] < long < mountain[1][1]:
        area = "mountain"
    elif pacific[0][0] < lat < pacific[0][1] and pacific[1][0] < long < pacific[1][1]:
        area = "pacific"
    else:
        area = ""
    return area


def compute_tuples(sentence, areaCount, areaKeys, keywordDict):
    # Function that returns the happiness score, number of keywords
    # and number of tweet computed in a sentence
    sentenceKey = 0
    sentenceHappy = 0
    areaCount += 1
    if bool(set(sentence).intersection(keywordDict)):
        areaKeys +=1
    for word in sentence:
        if word in keywordDict:
            sentenceHappy += keywordDict[word]
            sentenceKey += 1
    if sentenceKey != 0:
        sentenceScore = sentenceHappy/sentenceKey
    else:
        sentenceScore = 0
    return [sentenceScore, areaKeys, areaCount]


def compute_tweets(tweetsFile, keywordFile):
    # The main function

    try:
        # Test to see if the files inputted exist
        keywordLine = open(keywordFile,"r",encoding="utf-8")
        tweetsLine = open(tweetsFile, "r", encoding="utf-8")
        keywordLine.close()
        tweetsLine.close()
    except FileNotFoundError:
        # If a FileNotFoundError raises, the compute_tweets function
        # would return an empty list
        return []


    easternScore, centralScore, mountainScore, pacificScore = 0,0,0,0
    easternKeys, centralKeys, mountainKeys, pacificKeys = 0,0,0,0
    easternCount, centralCount, mountainCount, pacificCount = 0,0,0,0
        # Initialize all of the variables


    keywordLine = open(keywordFile,"r",encoding="utf-8")
    tweetsLine = open(tweetsFile, "r", encoding="utf-8")
        # Open the two files


    keywordDict = {}
        # Create a dictionary for the keywords where the keywords
        # are keys and the values are values

    for line in keywordLine:
            # Process the keyword file
        keyword, value = line.split(",")
        value = int(value.strip("\n"))
        keywordDict[keyword] = value


    for line in tweetsLine:
        # Read each line from the tweets file

        line = line.lower().split()
        # Convert the words into lower case letters and separate
        # them based on white space

        sentence = line[5:len(line)]
        # Get the sentence inside the line

        sentence = remove_punctuation(sentence)
        # Remove the punctuations with remove_punctuation function

        lat = float(line[0].strip("[,"))
        long = float(line[1].strip("]"))
        # Get the latitude and longitude of the tweet

        area = return_area(lat,long)
        # Get the name of the timezone of the tweet


        if area == "eastern":
            easternTuple = compute_tuples(sentence, easternCount, easternKeys, keywordDict)
            easternScore += easternTuple[0]
            easternCount = easternTuple[2]
            easternKeys = easternTuple[1]

        elif area == "central":
            centralTuple = compute_tuples(sentence, centralCount, centralKeys, keywordDict)
            centralScore += centralTuple[0]
            centralCount = centralTuple[2]
            centralKeys = centralTuple[1]

        elif area == "mountain":
            mountainTuple = compute_tuples(sentence, mountainCount, mountainKeys, keywordDict)
            mountainScore += mountainTuple[0]
            mountainCount = mountainTuple[2]
            mountainKeys = mountainTuple[1]

        elif area == "pacific":
            pacificTuple = compute_tuples(sentence, pacificCount, pacificKeys, keywordDict)
            pacificScore += pacificTuple[0]
            pacificCount = pacificTuple[2]
            pacificKeys = pacificTuple[1]

    if easternKeys != 0:
        easternAverage = easternScore/easternKeys # Gives out the happiness value
    else:
        easternAverage = 0
        # Gives out an happiness average of zero  when there is no keywords in
        # the timezone
    if centralKeys != 0:
        centralAverage = centralScore/centralKeys
    else: centralAverage = 0
    if mountainKeys != 0:
        mountainAverage = mountainScore/mountainKeys
    else:
        mountainAverage = 0
    if pacificKeys != 0:
        pacificAverage = pacificScore/pacificKeys
    else:
        pacificAverage = 0

    easternTuple = (easternAverage, easternKeys, easternCount)
    centralTuple = (centralAverage, centralKeys, centralCount)
    mountainTuple = (mountainAverage, mountainKeys, mountainCount)
    pacificTuple = (pacificAverage, pacificKeys, pacificCount)

    return [easternTuple, centralTuple, mountainTuple, pacificTuple]
