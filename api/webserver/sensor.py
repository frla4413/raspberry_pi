from flask import Blueprint, render_template
import api.webserver.python_scripts.template_data as template_data

sensor = Blueprint("sensor", __name__, static_folder="static", \
                                       template_folder="templates")

@sensor.route("/")
def home():
    return render_template('index.html')

@sensor.route("/sensors")
def sensors():
    data = template_data.get_sensor_data()
    return render_template('sensors.html', **data)

@sensor.route("/humidity")
def make_humidity_plot():
    data = template_data.get_humidity_data()
    return render_template('plot.html', **data)

@sensor.route("/temp")
def make_temperature_plot():
    data = template_data.get_temperature_data()
    return render_template('plot.html', **data)

@sensor.route("/raspberry_pi")
def raspberry_pi():
    return render_template("raspberry_pi.html")
