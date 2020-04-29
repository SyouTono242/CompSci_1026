from collections import defaultdict

initials, countries, incomes = [],[],[]

dict1 = {}
dict2 = defaultdict(set)

keywordFile = open("rawdata.txt", "r", encoding="utf-8")

for line in keywordFile:
    line = line.upper().strip("\n").split(":")
    initials.append(line[1][0])
    countries.append(line[1])
    incomes.append(line[2])

for i,country in enumerate(countries):
    dict1[country] = incomes[i]
    dict2[initials[i]].add(country)

userInput = input("Please enter a letter or the name of a country (enter \"quit\" to terminate):")
while userInput != "quit":
    userInput = userInput.upper()
    if len(userInput) == 1:
        print(dict2[userInput])
    elif userInput in countries:
        print("$",dict1[userInput])
    else:
        print("Does not exist.")
    userInput = input("Please enter a letter or the name of a country (enter \"quit\" to terminate):")
