import json


f1 = open("data/suicide_bombings.csv", "r")
lines = f1.readlines()

dictionary = {}
nestedDictKeys = lines[0].strip('\n').split(",") #selects the colomn header line and removes unnecessary characters

# Create the dictionary here
for i in range(1,len(lines)):
    line = lines[i].strip('\n') #selects line to work with and removes unnecessary characters

    splitLine = line.split(",") #splits the line into sections of data by ,

    dictionary[f"attack {i}"] = {} #creates nested dictionary to later be added to

    for j in range(len(splitLine)): # cycles through each peice of data for the specific attack
        dictionary[f"attack {i}"][nestedDictKeys[j]] = splitLine[j] #adds a category name in the dictionary paired with the corresponding data


f1.close()

#Save the json object to a file
f2 = open("data/suicide_bombings.json", "w")
json.dump(dictionary, f2, indent = 4)

f2.close()
