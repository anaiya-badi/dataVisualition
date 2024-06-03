# flask --app data_server run
from flask import Flask
from flask import request
from flask import render_template
import json


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    #load a current view of the data
    f = open("data/suicide_bombings.json", "r")
    data = json.load(f)
    f.close()

    g = open("data/country_alpha-2.json", "r")
    codes = json.load(g)
    g.close()

    #dropdown years
    attacks = list(data.keys())
    years = []
    countryTargetDict = {}
    countryColorDict = {}

    for attack in attacks:
        countryCode = codes[data[attack]["country"]]
        if data[attack]["year"] not in years:
            years.append(countryCode)
        if countryCode not in list(countryTargetDict.keys()):
            countryTargetDict[countryCode] = {}
            countryTargetDict[countryCode][attack] = data[attack]["target_type"]
        else:
            countryTargetDict[countryCode][attack] = data[attack]["target_type"]
    
    for country in list(countryTargetDict.keys()):
        rVal = 0
        gVal = 0
        bVal = 0
        civilianCount = 0
        securityCount = 0
        politicalCount = 0

        for attack in countryTargetDict[country]:
            if countryTargetDict[country][attack] == "Civilian":
                civilianCount += 1
            elif countryTargetDict[country][attack] == "Political":
                politicalCount += 1
            elif countryTargetDict[country][attack] == "Security":
                securityCount += 1
        
        rVal = civilianCount/(civilianCount+politicalCount+securityCount)
        gVal = securityCount/(civilianCount+politicalCount+securityCount)
        bVal = politicalCount/(civilianCount+politicalCount+securityCount)

        countryColorDict[country] = {}
        countryColorDict[country]["rVal"] = rVal*255
        countryColorDict[country]["gVal"] = gVal*255
        countryColorDict[country]["bVal"] = bVal*255

    #dropdown countries
    attacks = list(data.keys())
    countries = []

    for attack in attacks:
        if data[attack]["country"] not in countries:
            countries.append(data[attack]["country"])

    countries.sort()

    
    return render_template('index.html', years = countries, data = data, countryColorDict = countryColorDict)

@app.route('/micro')
def year():
    #load a current view of the data
    f = open("data/suicide_bombings.json", "r")
    data = json.load(f)
    f.close()

    g = open("data/country_alpha-2.json", "r")
    codes = json.load(g)
    g.close()

    requested_country = request.args.get('country')

    requested_code = codes[requested_country]

    #dropdown years
    attacks = list(data.keys())
    years = []
    countryTargetDict = {}
    countryNumsDict = {}

    for attack in attacks:
        countryCode = codes[data[attack]["country"]]
        if data[attack]["year"] not in years:
            years.append(countryCode)
        if countryCode not in list(countryTargetDict.keys()):
            countryTargetDict[countryCode] = {}
            countryTargetDict[countryCode][attack] = data[attack]["target_type"]
        else:
            countryTargetDict[countryCode][attack] = data[attack]["target_type"]
    
    for country in list(countryTargetDict.keys()):
        civilianCount = 0
        securityCount = 0
        politicalCount = 0

        for attack in countryTargetDict[country]:
            if countryTargetDict[country][attack] == "Civilian":
                civilianCount += 1
            elif countryTargetDict[country][attack] == "Political":
                politicalCount += 1
            elif countryTargetDict[country][attack] == "Security":
                securityCount += 1
        
        civ = civilianCount
        sec = securityCount
        pol = politicalCount

        countryNumsDict[country] = {}
        countryNumsDict[country]["civ"] = civ
        countryNumsDict[country]["sec"] = sec
        countryNumsDict[country]["pol"] = pol
        if civilianCount >= securityCount and civilianCount >= politicalCount:
            countryNumsDict[country]["most"] = "civ"
        if securityCount >= civilianCount and securityCount >= politicalCount:
            countryNumsDict[country]["most"] = "sec"
        if politicalCount >= civilianCount and politicalCount >= securityCount:
            countryNumsDict[country]["most"] = "pol"
            
    

    #dropdown countries
    attacks = list(data.keys())
    countries = []

    for attack in attacks:
        if data[attack]["country"] not in countries:
            countries.append(data[attack]["country"])

    countries.sort()



    totalAttacks = 0
    civAttacks = 0
    secAttacks = 0
    polAttacks = 0

    for country in list(countryNumsDict.keys()):
        civAttacks += countryNumsDict[country]["civ"]
        secAttacks += countryNumsDict[country]["sec"]
        polAttacks += countryNumsDict[country]["pol"]
        totalAttacks += countryNumsDict[country]["civ"] + countryNumsDict[country]["sec"] + countryNumsDict[country]["pol"]

    civAverage = civAttacks/totalAttacks
    secAverage = secAttacks/totalAttacks
    polAverage = polAttacks/totalAttacks

    return render_template('micro.html', years = countries, requested_country = requested_country, requested_code = requested_code, countryNumsDict = countryNumsDict, civAverage = civAverage, secAverage = secAverage, polAverage = polAverage)

@app.route('/about')
def about():
    #load a current view of the data
    f = open("data/suicide_bombings.json", "r")
    data = json.load(f)
    f.close()

    #dropdown countries
    attacks = list(data.keys())
    countries = []

    for attack in attacks:
        if data[attack]["country"] not in countries:
            countries.append(data[attack]["country"])

    countries.sort()

    return render_template('about.html', years = countries)

app.run(debug=True)
