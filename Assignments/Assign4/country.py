#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Yiran Shao"
__email__ = "yshao242@uwo.ca"
__status__ = "Prototype"

###
# This program implements a class Country
# that holds the information about a single country


class Country:

    # Constructor method
    def __init__(self, name = "", pop = 0, area = 0, continent = ""):
        self._name = name
        self._pop = pop
        self._area = area
        self._continent = continent

    # Repr method that generates a string representation
    # for class objects in a readable fashion
    def __repr__(self):
        reprString = "{0} (pop: {1}, size: {2}) in {3}\n".format(self._name, self._pop, self._area, self._continent)
        return reprString

    # Getter methods
    def getName(self):
        return self._name
    def getPopulation(self):
        return self._pop
    def getArea(self):
        return self._area
    def getContinent(self):
        return self._continent

    # Setter methods
    def setPopulation(self,pop):
        self._pop = pop
    def setArea(self, area):
        self._area = area
    def setContinent(self, continent):
        self._continent = continent
