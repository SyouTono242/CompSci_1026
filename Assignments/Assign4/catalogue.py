#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Yiran Shao"
__email__ = "yshao242@uwo.ca"
__status__ = "Prototype"

###
# This program implements a class called CountryCatalogue
# that uses a file to build the data structures to hold the
# information about countries

from country import Country

# A dictionary of the countries
countryCat = {}

class CountryCatalogue:

    # Constructor that takes the name of the file that contains
    # the information about each country and uses the data in
    # the file to construct the dictionary countryCat
    def __init__(self, countryFile):
        self._file = open(countryFile,"r",encoding="utf-8")
        self._file.readline()
        for line in self._file:
            # Checks if the line contains three vertical bars
            if line.count("|") == 3:
                name, continent, pop, area = line.split("|")
                pop = pop.replace(",","")
                area = area.replace(",","").strip("\n")
                countryObject = Country(name, pop, area, continent)
                countryCat[name.title()] = countryObject
        self._file.close()

    # Setter methods
    def setPopulationOfCountry(self, name, pop):
        if name.title() in countryCat:
            countryCat[name].setPopulation(pop)
    def setAreaOfCountry(self, name, area):
        if name.title() in countryCat:
            countryCat[name].setArea(area)
    def setContinentOfCountry(self, name, continent):
        if name.title() in countryCat:
            countryCat[name].setContinent(continent)

    # findCountry method that checks to see if the country
    # object is in countryCat
    def findCountry(self, country):
        if country in countryCat:
            return country
        else:
            return None

    # addCountry method that adds a new country to countryCat
    def addCountry(self, newName, newPop, newArea, newContinent):
        # checks if the country already exists in countryCat
        if newName.title() not in countryCat:
            countryObject = Country(newName, newPop, newArea, newContinent)
            countryCat[newName.title()] = countryObject
            # returns True when the operation is successful
            return True
        else:
            # returns False when the country already exists
            return False

    # printCountryCatalogue method that prints a list of the
    # countries and their information to the screen
    def printCountryCatalogue(self):
        print(countryCat.__repr__())

    # saveCountryCatalogue method that saves all the country
    # information in the catalogue to a file in the same
    # format as the original file
    def saveCountryCatalogue(self, fname):
        try:
            file = open(fname,"w")
            count = 0
            file.write("Country|Continent|Population|Area\n")
            for country in sorted(countryCat):
                count = count + 1
                name = countryCat[country].getName()
                continent = countryCat[country].getContinent
                population = countryCat[country].getPopulatiuon
                area = countryCat[country].getArea()
                output = "{0}|{1}|{2}|{3}\n".format(name, continent, population, area)
                file.write(output)
        except:
            count = -1

        # opens the file that saves all the country information
        file = open(fname,"w")
        # initialization of the counter
        count = 0
        # writes the header of the file
        file.write("Country|Continent|Population|Area\n")
        # sort all of the countries alphabetically by name prior
        # to saving
        for country in sorted(countryCat):
            # count the number of items written
            count = count + 1
            name = countryCat[country].getName()
            continent = countryCat[country].getContinent()
            population = countryCat[country].getPopulation()
            area = countryCat[country].getArea()
            if population != "":
                # add thousands separators in population number
                population = format(int(population),",")
            if area != "":
                # add thousands separators in area number
                area = format(int(area),",")
            # write one line in the file
            output = "{0}|{1}|{2}|{3}\n".format(name, continent, population, area)
            file.write(output)
        file.close()
        return count

