

#################################################
# Dependencies
#################################################
import numpy as np
import sqlite3
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text
import datetime as dt
import pandas as pd
from flask import Flask, jsonify, render_template

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/Final_Obesity.db")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table

covid = Base.classes.covid
linechartdata = Base.classes.confirmed
deaths = Base.classes.deaths
# Create our session (link) from Python to the DB
session = Session(engine)



app = Flask(__name__)

#################################################
# Flask Routes
#################################################

#################################################
# HOME PAGE
#################################################
@app.route('/')
def home():
   return render_template('index.html')

#################################################
# MAP
#################################################
@app.route('/map')
def map():
   return render_template('map.html')

#################################################
# covid page
#################################################
@app.route('/covid')
def Covid2():
   return render_template('covid.html')


# #################################################
# # Covid ENDPOINT
# #################################################
@app.route('/covid/info')
def covidinfo():
     # Create our session (link) from Python to the DB
    session = Session(engine)
    # Query all
    results1 = session.query(covid.St, covid.population, covid.TTL_Obease).all()     
                            
    session.close()
    # Create a dictionary from the row data and append to a list of all_rates
    df = pd.DataFrame(results1)
    States = list(df["St"])
    categories_and_values = {}
    for rname in States:
        rates_series = df.loc[df["St"]==rname].iloc[:,1:]
        rates_values = list(rates_series.values[0])
        rates_years = ['Population','TTL Obease']
        categories_and_values[rname] = {"Rates":rates_values, "Years": rates_years}
    print(categories_and_values)
   
    
    return categories_and_values
# #################################################
# # Covid ENDPOINT
# #################################################
@app.route('/covid/info2')
def covidinfo2():
     # Create our session (link) from Python to the DB
    
    session = Session(engine)
    results = session.query(linechartdata.St, linechartdata.Col_1_2020, linechartdata.Col_6_2020, linechartdata.Col_1_2021, linechartdata.Col_6_2021, linechartdata.Col_1_2022, linechartdata.Col_6_2022, linechartdata.Col_1_2023).all()
    session.close()

    df = pd.DataFrame(results)
    rate_names = list(df["St"])
    categories_and_values = {}
    for rname in rate_names:
        rates_series = df.loc[df["St"]==rname].iloc[:,1:]
        rates_values = list(rates_series.values[0])
        rates_years = ['Jan2020', 'Jun2020', 'Jan2021', 'Jun2021', 'Jan2022', 'Jun2022', 'Jan2023']
        categories_and_values[rname] = {"Rates":rates_values, "Years": rates_years}
    print(categories_and_values)
    
    return categories_and_values

# #################################################
# # Covid ENDPOINT
# #################################################
@app.route('/covid/info3')
def covidinfo3():
     # Create our session (link) from Python to the DB
    
    session = Session(engine)
    results = session.query(deaths.St, deaths.Col_1_2020, deaths.Col_6_2020, deaths.Col_1_2021, deaths.Col_6_2021, deaths.Col_1_2022, deaths.Col_6_2022, deaths.Col_1_2023).all()
    session.close()

    df = pd.DataFrame(results)
    rate_names = list(df["St"])
    categories_and_values = {}
    for rname in rate_names:
        rates_series = df.loc[df["St"]==rname].iloc[:,1:]
        rates_values = list(rates_series.values[0])
        rates_years = ['Jan2020', 'Jun2020', 'Jan2021', 'Jun2021', 'Jan2022', 'Jun2022', 'Jan2023']
        categories_and_values[rname] = {"Rates":rates_values, "Years": rates_years}
    print(categories_and_values)
    
    return categories_and_values



if __name__ == '__main__':
    app.run(port=8000, debug=False)