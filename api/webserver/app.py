''' This program print Hello and output the current time
To run:
    o on pi: sudo python3 app.py
    o on another computer/phon connected to the wifi: 192.168.0.13
      (use a browser)
    '''

from flask import Flask, render_template
import datetime
import socket
from gpiozero import CPUTemperature
import netifaces
from sensors.utils import get_last_reading
import sensors.cpu_temperature.cpu_temperature as cpu_temp

app = Flask(__name__)

def get_time():
   current_time = datetime.datetime.now()
   return current_time.strftime("%Y-%m-%d %H:%M")

def get_cpu_temp():
    return CPUTemperature().temperature

def get_ip_address():
    wlan_info = netifaces.ifaddresses('wlan0')
    return wlan_info[2][0]['addr']

def get_temp_humidity():
    filename = '/home/pi/Documents/raspberry_pi/sensors/dht11/data.csv'
    last_reading = get_last_reading(filename).split(',')
    time = last_reading[0]
    temp = last_reading[1]
    humidity = last_reading[2]
    return time, humidity, temp

@app.route("/")
def status():

    name = 'raspberry pi' + " (" + get_ip_address() + ")"
    sensor_time, humidity, temp = get_temp_humidity()
    templateData = {
        'title' : 'Time and temp!',
        'time': get_time(),
        'name': name,
        'temp_sensor': temp,
        'humidity': humidity,
        'temp_sensor_time': sensor_time,
        'cpu_temp': cpu_temp.get_temp()
      }
    return render_template('index.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
