# flask --app data_server run
from flask import Flask
from flask import request
from flask import render_template
import json


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    #load a current view of the data
    f = open("data/life_expectancy.json", "r")
    data = json.load(f)
    f.close()

    #check to see if year is in the query string portion of the URL
    requested_year = request.args.get('year')
    if requested_year == None:
        requested_year = "1975" #just in case

    #Filter and reformat data for ease of access in the template
    years = list(data.keys())
    requested_data = {}
    for year in years:
        requested_data[year] = data[year][requested_year]
    all_years = sorted(list(data[years[0]].keys()))    


    #US points
    us_line_endpoints =[]
    for i in range(len(all_years)-1): # make it easy to dynamically generate a line graph
        start_x = all_years[i] #generate endpoints for each line segment
        stop_x = all_years[i+1]
        us_line_endpoints.append([data["United States"][start_x], data["United States"][stop_x]])

    #Canada points
    canada_line_endpoints =[]
    for i in range(len(all_years)-1): # make it easy to dynamically generate a line graph
        c_start_x = all_years[i] #generate endpoints for each line segment
        c_stop_x = all_years[i+1]
        canada_line_endpoints.append([data["Canada"][c_start_x], data["Canada"][c_stop_x]])

    #Mexico points
    mexico_line_endpoints =[]
    for i in range(len(all_years)-1): # make it easy to dynamically generate a line graph
        m_start_x = all_years[i] #generate endpoints for each line segment
        m_stop_x = all_years[i+1]
        mexico_line_endpoints.append([data["Mexico"][m_start_x], data["Mexico"][m_stop_x]])
    
    #Universal average
    total_ages = 0
    year_count = len(all_years)-1
    year3_count = year_count * 3
    for i in range(year_count): # make it easy to dynamically generate a line graph
        total_ages = total_ages + data["Canada"][all_years[i]] +  data["United States"][all_years[i]] +  data["Mexico"][all_years[i]]
    universal_average = total_ages / year3_count

    
    return render_template('index.html', all_years = all_years, us_endpoints = us_line_endpoints, canada_endpoints = canada_line_endpoints, mexico_endpoints = mexico_line_endpoints, universal_life_average = universal_average)

@app.route('/year')
def year():
    #load a current view of the data
    f = open("data/life_expectancy.json", "r")
    data = json.load(f)
    f.close()

    #check to see if year is in the query string portion of the URL
    requested_year = request.args.get('year')
    if requested_year == None:
        requested_year = "1975" #just in case
    
    canada_average = data["Canada"][requested_year]
    us_average = data["United States"][requested_year]
    mexico_average = data["Mexico"][requested_year]

    for i in range(55, 85, 3):
        if canada_average >= i and canada_average <= i+3:
            canada_color = (i-50)*5
        
        if us_average >= i and us_average <= i+3:
            us_color = (i-50)*5
        
        if mexico_average >= i and mexico_average <= i+3:
            mexico_color = (i-50)*5

    smallest_expectancy_text = "Canada had the smallest life expectancy in "

    if us_average < canada_average:
        smallest_expectancy_text = "The United States had the smallest life expectancy in "
        if mexico_average < canada_average:
            smallest_expectancy_text = "Mexico had the smallest life expectancy in "
    elif mexico_average < canada_average:
        smallest_expectancy_text = "Mexico had the smallest life expectancy in "
    
    return render_template('year.html', requested_year = requested_year, canada_color = canada_color, us_color = us_color, mexico_color = mexico_color,  canada_average = round(canada_average,1), us_average = round(us_average,1), mexico_average = round(mexico_average,1), smallest_expectancy_text = smallest_expectancy_text)

app.run(debug=True)
