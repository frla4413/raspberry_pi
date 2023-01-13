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
def make__humidity_plot():

    data = json.loads(data_base.get_temp_humidity())
    df = pd.DataFrame(data)

    fig = px.line(df, x="Time", y=df.columns[1:3])
    fig.show()
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Humidity at home"
    description = """
    Wow! Sure looks humid enough!
    """
    return render_template('plot.html', graphJSON=graphJSON, header=header,description=description)

@app.route("/temp")
def make__temperature_plot():

    data = json.loads(data_base.get_temp_humidity())
    df = pd.DataFrame(data)

    fig = px.line(df, x="Time", y="Temp")
    fig.show()
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Temperature at home"
    description = """
    Wow! Sure looks hot in here!
    """
    return render_template('plot.html', graphJSON=graphJSON, header=header,description=description)


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
