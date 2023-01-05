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

app = Flask(__name__)

def get_time():
   current_time = datetime.datetime.now()
   return current_time.strftime("%Y-%m-%d %H:%M")

def get_cpu_temp():
    return CPUTemperature().temperature

def get_ip_address():
    wlan_info = netifaces.ifaddresses('wlan0')
    return wlan_info[2][0]['addr']

@app.route("/")
def status():
   name = 'raspberry pi' + " (" + get_ip_address() + ")"
   templateData = {
      'title' : 'Time and temp!',
      'time': get_time(),
      'name': name,
      'temp': get_cpu_temp()
      }
   return render_template('index.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
