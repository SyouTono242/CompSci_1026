#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Yiran Shao"
__email__ = "yshao242@uwo.ca"
__status__ = "Prototype"


###
# This module implements a function
# processUpdates(cntryFileName,updateFileName) that updates
# the country file given with the update file

import os
from catalogue import CountryCatalogue


# A helper function that writes the output file differently
# base on whether the update is successful and returns the
# number of items written
def output_file(success,cntryCatalogue):
    outputFile = open("output.txt", "w+")
    if success:
        count = cntryCatalogue.saveCountryCatalogue("output.txt")
    else:
        # write the message "Update Unsuccessful\n" to the
        # file “output.txt” when the update is unsuccessful
        outputFile.write("Update Unsuccessful\n")
        count = -1
    outputFile.close()
    return count

# The processUpdates function that takes the names of the two
# files and gives out a output file with updated data
def processUpdates(cntryFileName,updateFileName):

    # check whether the country file exists
    while os.path.isfile(cntryFileName) is False:
        # print a message telling the user that the file name
        # inputted does not exist
        print("Country file: {} not found.".format(cntryFileName))
        # ask whether the user wishes to quit the program
        quitChoice = input("Do you wish to quit now? (Y/N)")
        # prompt the user to enter a correct name of the country file
        if quitChoice == "N":
            cntryFileName = input("Enter name of file with country data:")
        else:
            success = False
            output_file(success, None)
            return False
    else:
        cntryCatalogue = CountryCatalogue(cntryFileName)

        # checks whether the update file exists
        while os.path.isfile(updateFileName) is False:
            # print a message when the update file does not exist
            print("Update file: {} not found.".format(updateFileName))
            # ask whether the user wishes to quit
            quitChoice = input("Do you wish to quit now? (Y/N)")
            # prompt the user to enter a correct name of the update file
            if quitChoice == "N":
                updateFileName = input("Enter name of file with country updates:")
            else:
                success = False
                output_file(success, None)
                return False

        # update the file when both the country file and update file exist
        else:
            updateFile = open(updateFileName, "r", encoding="utf-8")
            for line in updateFile:
                line = line.strip("\n")
                words = line.split(";")
                name = words[0]

                # update the data when the country already exist in the
                # country file
                if cntryCatalogue.findCountry(name) is not None:
                    for word in words[1:len(words)]:
                        # remove all of the extra spaces
                        word = word.replace(" ","")
                        if word[0] == "P":
                            pop = int(word[2:len(word)].replace(",",""))
                            cntryCatalogue.setPopulationOfCountry(name,pop)
                        if word[0] == "A":
                            area = int(word[2:len(word)].replace(",",""))
                            cntryCatalogue.setAreaOfCountry(name,area)
                        if word[0] == "C":
                            continent = str(word[2:len(word)])
                            cntryCatalogue.setContinentOfCountry(name,continent)
                # create a new country when it did not exist in the country
                # file
                else:
                    # initialization of the pop, area and continent
                    pop, area, continent = "","",""
                    for word in words[1:len(words)]:
                        word = word.replace(" ","")
                        if word[0] == "P":
                            pop = int(word[2:len(word)].replace(",",""))
                        if word[0] == "A":
                            area = int(word[2:len(word)].replace(",",""))
                        if word[0] == "C":
                            continent = word[2:len(word)]
                    cntryCatalogue.addCountry(name, pop, area, continent)
        success = True
        count = output_file(success,cntryCatalogue)
        return True
