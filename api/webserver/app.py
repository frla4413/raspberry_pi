''' This program print Hello and output the current time
To run:
    o on pi: sudo python3 app.py
    o on another computer/phon connected to the wifi: 192.168.0.13
      (use a browser)
    '''
from flask import Flask, render_template, url_for
import plotly.express as px
import plotly
import json
import pandas as pd
import sensors.get_data as data_base
import api.webserver.python_scripts.template_data as template_data2

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/sensors")
def sensors():
    data = template_data2.get_sensor_data()
    return render_template('sensors.html', **data)

@app.route("/humidity")
def make_humidity_plot():
    data = template_data2.get_humidity_data()
    return render_template('plot.html', **data)

@app.route("/temp")
def make_temperature_plot():
    data = template_data2.get_temperature_data()
    return render_template('plot.html', **data)

@app.route("/raspberry_pi")
def raspberry_pi():
    return render_template("raspberry_pi.html")

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
