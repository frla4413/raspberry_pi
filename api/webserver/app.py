''' This program print Hello and output the current time
To run:
    o on pi: sudo python3 app.py
    o on another computer/phon connected to the wifi: 192.168.0.13
      (use a browser)
    '''
from flask import Flask, render_template
import plotly.express as px
import plotly
import json
import pandas as pd
import sensors.get_data as data_base

app = Flask(__name__)

@app.route("/")
def status():
    return render_template('index.html')

@app.route("/sensors")
def sensors():
    template_data = json.loads(data_base.get_last_data())
    return render_template('sensors.html', **template_data)

@app.route("/humidity")
def make_humidity_plot():

    data = json.loads(data_base.get_temp_humidity())
    df = pd.DataFrame(data)

    fig = px.line(df, x="Time", y="Humidity")
    fig.show()
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    template_data = {"title": "Humidity",
                     "header": "Humidity at home",
                     "description": "Wow! Sure looks humid in here!",
                     "graphJSON": graphJSON}
    return render_template('plot.html', **template_data)

@app.route("/temp")
def make_temperature_plot():

    data = json.loads(data_base.get_temp_humidity())
    df = pd.DataFrame(data)

    fig = px.line(df, x="Time", y="Temp")
    fig.show()
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    template_data = {"title": "Temperature",
                     "header": "Temperature at home",
                     "description": "Wow! Sure looks hot in here!",
                     "graphJSON": graphJSON}

    return render_template('plot.html', **template_data)

@app.route("/base")
def home():
    return render_template("bootstap2.html")

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
