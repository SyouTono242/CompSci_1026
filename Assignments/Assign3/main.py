#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Yiran Shao"
__email__ = "yshao242@uwo.ca"
__status__ = "Prototype"

##
# The program prompt the user for the name of the
# two files (tweets file and the keywords file).
# It then calls the function compute_tweet in
# sentiment_analysis.py with the two files to process
# the tweets using the given keywords.
# Hopefully, it should print the results in a readable fashion.
#

from sentiment_analysis import *

tweetsFile = input("Please enter the name of the file with the tweets:")
keywordFile = input("Please enter the name of the file with the keywords:")
    # Prompt the user for the name of the file
keywordList = compute_tweets(tweetsFile, keywordFile)
    # Use the compute_tweets to process the files
print()

if keywordList:
    # Check if the compute_tweet function returns an empty list
    areaList = ["Eastern","Central","Mountain","Pacific"]
    for i in areaList:
        print(i,"Time Zone happiness score:","%7.3f" %(keywordList[areaList.index(i)][0]),";",
                "found","%4.0f" %keywordList[areaList.index(i)][1],"tweets.")
        # Print out the happiness score and total number of tweets of each timezone
else:
    raise FileNotFoundError
    # Raise a file-not-found-error if the compute_tweets return an empty list
