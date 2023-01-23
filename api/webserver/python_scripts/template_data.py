import plotly.express as px
import plotly
import json
import pandas as pd
import sensors.get_data as data_base
from datetime import datetime

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

class Vitamiens:
    def __init__(self, name):
        self.name = name
        self.date_taken = None

    def __str__(self):
        if self.date_taken == datetime.today().date():
            return f"You have taken {self.name} today ({self.date_taken})"
        if self.date_taken is None: 
            return f"You have never taken {self.name}."
        return f"You have not taken {self.name} today. Last taken {self.date_taken}. "

    def take_vitamine(self):
        self.date_taken = datetime.today().date()

if __name__ == "__main__":
    v = Vitamiens("Multi")
    print(v)
    v.take_vitamine()
    print(v)
