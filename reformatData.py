import json


f1 = open("data/suicide_bombings.csv", "r")
lines = f1.readlines()

dictionary = {}

# Create the dictionary here
for i in range(0,len(lines)):
    line = lines[i]

    splitLine = line.split(",") #splits the line into sections of data by ,

    dictionary[f"attack {i}"] = (splitLine)

f1.close()

#Save the json object to a file
f2 = open("data/suicide_bombings.json", "w")
json.dump(dictionary, f2, indent = 4)

f2.close()