import datetime
import netifaces
import json
import os
import csv

import sensors.cpu_temperature.cpu_temperature as cpu_temp
import sensors.utils as utils

def get_last_reading(filename):
    with open(filename, 'rb') as f:
        try:  # catch OSError in case of a one line file
            f.seek(-2, os.SEEK_END)
            while f.read(1) != b'\n':
                f.seek(-2, os.SEEK_CUR)
        except OSError:
            f.seek(0)
        last_reading = f.readline().decode()
    return last_reading

def get_time():
   current_time = datetime.datetime.now()
   return current_time.strftime("%Y-%m-%d %H:%M")

def get_ip_address():
    wlan_info = netifaces.ifaddresses('wlan0')
    return wlan_info[2][0]['addr']

def get_last_soil_moisture_reading(filename):
    last_reading = get_last_reading(filename).split(',')
    time = last_reading[0]
    moisture = last_reading[1][0:4]
    return time, moisture

def get_last_dht11_reading(filename):
    last_reading = get_last_reading(filename).split(',')
    time = last_reading[0]
    temp = last_reading[1]
    humidity = last_reading[2]
    return time, humidity, temp

def get_last_temp_humidity():
    filename = '/home/pi/Documents/raspberry_pi/sensors/dht11/data.csv'
    return get_last_dht11_reading(filename)

def get_last_soil_moisture():
    filename = '/home/pi/Documents/raspberry_pi/sensors/soil_moisture/data.csv'
    return get_last_soil_moisture_reading(filename)

def get_last_data():
    name = 'raspberry pi' + " (" + get_ip_address() + ")"
    temp_sensor_time, humidity, temp = get_last_temp_humidity()
    moisture_time, moisture = get_last_soil_moisture()
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
    return json.dumps(sensor_data, indent = 4)

def get_temp_humidity():
    filename = '/home/pi/Documents/raspberry_pi/sensors/dht11/data.csv'
    with open(filename, newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        time = []
        temp = []
        humidity = []
        for row in reader:
            if row[-1] in ['True']:
                time.append(row[0])
                temp.append(row[1])
                humidity.append(row[2])

    return json.dumps({'Time': time[1:], 'Temp': temp[1:], 'Humidity':humidity[1:]}, indent = 4)
if __name__ == '__main__':
    print(get_last_data())
