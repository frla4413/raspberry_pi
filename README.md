**Raspberry pi, sensors and API**

The purpose of this project is to learn electronics and API and to combine the two.

**Sensors:**
* Temperature sensor DS18B20
* Temperature and humidity sensor dht11

**Remember:** 
* Add PYTHONPATH=/home/pi/Documents/raspberry_pi/ to .bashrc/.zshrc
* Must also add PYTHONPATH to /etc/sudoers (since the api-app is executed in sudo-mode)
  * Add: Defaults        env_keep += 'PYTHONPATH
  * Remove: env_reset
  * see here: https://stackoverflow.com/questions/7969540/pythonpath-not-working-for-sudo-on-gnu-linux-works-for-root
