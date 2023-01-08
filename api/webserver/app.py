''' This program print Hello and output the current time
To run:
    o on pi: sudo python3 app.py
    o on another computer/phon connected to the wifi: 192.168.0.13
      (use a browser)
    '''

from flask import Flask, render_template
from gpiozero import CPUTemperature
import api.webserver.python_scripts.data_scripts as data_scripts

app = Flask(__name__)

@app.route("/")
def status():
    template_data = data_scripts.get_data()
    return render_template('index.html', **template_data)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
