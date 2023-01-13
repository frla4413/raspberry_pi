import datetime
import netifaces
import json

from sensors.utils import get_last_reading
import sensors.cpu_temperature.cpu_temperature as cpu_temp
import sensors.utils as utils

def get_time():
   current_time = datetime.datetime.now()
   return current_time.strftime("%Y-%m-%d %H:%M")

def get_ip_address():
    wlan_info = netifaces.ifaddresses('wlan0')
    return wlan_info[2][0]['addr']

def get_temp_humidity():
    filename = '/home/pi/Documents/raspberry_pi/sensors/dht11/data.csv'
    return utils.get_last_dht11_reading(filename)

def get_temp2():
    return json.dumps(get_temp_humidity(), indent = 4)

def get_soil_moisture():
    filename = '/home/pi/Documents/raspberry_pi/sensors/soil_moisture/data.csv'
    return utils.get_last_soil_moisture_reading(filename)

def get_data():
    name = 'raspberry pi' + " (" + get_ip_address() + ")"
    temp_sensor_time, humidity, temp = get_temp_humidity()
    moisture_time, moisture = get_soil_moisture()
    sensor_data = {
        'title' : 'Time and temp!',
        'time': get_time(),
        'name': name,
        'temp_sensor': temp,
        'humidity': humidity,
        'temp_sensor_time': temp_sensor_time,
        'moisture_sensor_time': moisture_time,
        'moisture': moisture,
        'cpu_temp': cpu_temp.get_temp()
      }
    return sensor_data


if __name__ == '__main__':
    print(get_temp2())
