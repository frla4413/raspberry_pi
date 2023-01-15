import plotly.express as px
import plotly
import json
import pandas as pd
import sensors.get_data as data_base

def get_sensor_data():
    return json.loads(data_base.get_last_data())

def get_humidity_data():
    data = json.loads(data_base.get_temp_humidity())
    df = pd.DataFrame(data)

    fig = px.line(df, x="Time", y="Humidity")
    fig.show()
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return {"title": "Humidity",
            "header": "Humidity at home",
            "description": "Wow! Sure looks humid in here!",
            "graphJSON": graphJSON}

def get_temperature_data():
    data = json.loads(data_base.get_temp_humidity())
    df = pd.DataFrame(data)

    fig = px.line(df, x="Time", y="Temp")
    fig.show()
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return {"title": "Temperature",
            "header": "Temperature at home",
            "description": "Wow! Sure looks hot in here!",
            "graphJSON": graphJSON}
