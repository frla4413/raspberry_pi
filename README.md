**Raspberry pi, sensors and API**

The purpose of this project is to learn electronics and API and to combine the two.

**Sensors:**
* Temperature sensor DS18B20
* Temperature and humidity sensor dht11

**Remember:**
* Add PYTHONPATH=/home/pi/Documents/raspberry_pi/ to .bashrc/.zshrc
* Must also add PYTHONPATH to /etc/sudoers (since the api-app is executed in sudo-mode)
  * To run in sudo: sudo~/.virtualenv/env/bin/python3 app.py
  * Add: Defaults env_keep += 'PYTHONPATH
  * Remove: env_reset
  * see here: https://stackoverflow.com/questions/7969540/pythonpath-not-working-for-sudo-on-gnu-linux-works-for-root
* Virtualenvs:
  * api
  * sensors_dev

**TODO:**
* Draw termometer figure with pygame
* virtualenv
* Fritzing for drawing
* LED (https://projects.raspberrypi.org/en/projects/people-in-space-indicator/0)
* Graphs (plotly + Flask: https://towardsdatascience.com/web-visualization-with-plotly-and-flask-3660abf9c946)
* Have installed some python packages as sudo --> see sudo pip3 freeze. Problem with plotly as sudo
  Add a user to sudo with restrictions?
* Check bootstrap for presenting images (Matildas drawings, Raspberry pi with fritzing)

**TUTORIALS**
* Tech with tim -- Flask tutorial

NEED TO RUN outside of venv --> must have packages installed via apt and run as root
sudo ptyhon3.7 app.py
