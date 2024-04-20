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

    #dropdown years
    attacks = list(data.keys())
    years = []

    for attack in attacks:
        if data[attack]["year"] not in years:
            years.append(data[attack]["year"])

    years.sort()

    
    return render_template('index.html', years = years)

@app.route('/micro')
def year():
    #load a current view of the data
    f = open("data/suicide_bombings.json", "r")
    data = json.load(f)
    f.close()

    requested_year = request.args.get('year')

    #dropdown years
    attacks = list(data.keys())
    years = []

    for attack in attacks:
        if data[attack]["year"] not in years:
            years.append(data[attack]["year"])

    years.sort()

    return render_template('micro.html', years = years, requested_year = requested_year)

@app.route('/about')
def about():
    #load a current view of the data
    f = open("data/suicide_bombings.json", "r")
    data = json.load(f)
    f.close()

    #dropdown years
    attacks = list(data.keys())
    years = []

    for attack in attacks:
        if data[attack]["year"] not in years:
            years.append(data[attack]["year"])

    years.sort()

    return render_template('about.html', years = years)

app.run(debug=True)
