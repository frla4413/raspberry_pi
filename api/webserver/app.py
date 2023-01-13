''' This program print Hello and output the current time
To run:
    o on pi: sudo python3 app.py
    o on another computer/phon connected to the wifi: 192.168.0.13
      (use a browser)
    '''
from flask import Flask, render_template
import api.webserver.python_scripts.data_scripts as data_scripts
import plotly.express as px
import plotly
import json
import pandas as pd


app = Flask(__name__)

@app.route("/")
def status():
    return render_template('index.html')

@app.route("/sensors")
def sensors():
    template_data = data_scripts.get_data()
    return render_template('sensors.html', **template_data)

@app.route("/plots")
def make_plot():

   df = pd.DataFrame({
        'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges', 'Bananas'],
        'Amount': [4, 1, 2, 2, 4, 5],
        'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']})

   fig = px.bar(df, x='Fruit', y='Amount', color='City', barmode='group')
   graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
   return render_template('figure.html', graphJSON=graphJSON)
#
#
#    file_name = '/home/pi/Documents/raspberry_pi/sensors/dht11/data.csv'
#    df = pd.read_csv(file_name, sep=',')
#    fig = px.line(df, x="Time", y="Humidity")
#    fig.show()
#    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
#    header="Humidity at home"
#    description = """
#    Wow! Sure looks humid enough!
#    """
#    return render_template('notdash2.html', graphJSON=graphJSON, header=header,description=description)


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
