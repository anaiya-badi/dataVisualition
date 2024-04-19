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

    
    return render_template('index.html')

@app.route('/micro')
def year():
    #load a current view of the data
    f = open("data/suicide_bombings.json", "r")
    data = json.load(f)
    f.close()

    
    return render_template('micro.html')

@app.route('/about')
def about():
    return render_template('about.html')

app.run(debug=True)
