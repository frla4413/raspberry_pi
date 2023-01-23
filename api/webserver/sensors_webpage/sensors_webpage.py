from flask import Blueprint, render_template
import api.webserver.python_scripts.template_data as template_data

sensors_webpage = Blueprint("sensors_webpage", __name__, static_folder="static", \
                                                         template_folder="templates")

@sensors_webpage.route("/")
def home():
    return render_template('sensor_index.html')

@sensors_webpage.route("/sensors")
def sensors():
    data = template_data.get_sensor_data()
    return render_template('sensors.html', **data)

@sensors_webpage.route("/humidity")
def make_humidity_plot():
    data = template_data.get_humidity_data()
    return render_template('plot.html', **data)

@sensors_webpage.route("/temp")
def make_temperature_plot():
    data = template_data.get_temperature_data()
    return render_template('plot.html', **data)

@sensors_webpage.route("/raspberry_pi")
def raspberry_pi():
    return render_template("raspberry_pi.html")
