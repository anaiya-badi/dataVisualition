import json
import math


f1 = open("data/suicide_bombings.csv", "r")
lines = f1.readlines()

dictionary = {}
nestedDictKeys = lines[0].strip('\n').split(",") #selects the colomn header line and removes unnecessary characters

# Create the dictionary here
for i in range(1,len(lines)):
    line = lines[i].strip('\n') #selects line to work with and removes unnecessary characters

    splitLine = line.split(",") #splits the line into sections of data by ,

    dictionary[f"attack {i}"] = {} #creates nested dictionary to later be added to

    for j in range(len(splitLine)): # cycles through each piece of data for the specific attack
        if nestedDictKeys[j] == "#wounded" or nestedDictKeys[j] == "#killed" or nestedDictKeys[j] == "#killed_civilian" or nestedDictKeys[j] == "#killed_political" or nestedDictKeys[j] == "#killed_security":
            dictionary[f"attack {i}"][nestedDictKeys[j]] = math.ceil(float(splitLine[j])) #adds a category name in the dictionary paired with the rounded up corresponding data
        else: 
            dictionary[f"attack {i}"][nestedDictKeys[j]] = splitLine[j] #adds a category name in the dictionary paired with the corresponding data


f1.close()

#Save the json object to a file
f2 = open("data/suicide_bombings.json", "w")
json.dump(dictionary, f2, indent = 4)

f2.close()

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


f1 = open("data/country_alpha-2.csv", "r")
lines = f1.readlines()

dictionary = {}

# Create the dictionary here
for i in range(0,len(lines)):
    line = lines[i].strip('\n') #selects line to work with and removes unnecessary characters

    splitLine = line.split(",") #splits the line into sections of data by ,

    dictionary[splitLine[0]] = splitLine[1].lower()#creates nested dictionary to later be added to

f1.close()

#Save the json object to a file
f2 = open("data/country_alpha-2.json", "w")
json.dump(dictionary, f2, indent = 4)

f2.close()
