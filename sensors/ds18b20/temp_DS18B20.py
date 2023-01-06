''' code for the temperature sensor is taken from:
https://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/

This script reads the cpu-temp, reads the temp from the ds18b20-sensor and
writes it to a file. The result is also printed to the terminal.
'''

import os
import glob
from time import sleep, strftime, time
from gpiozero import CPUTemperature

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'

device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

cpu = CPUTemperature()
path = "/home/pi/Documents/temp.csv"
path = "temp.csv"
with open(path, "a") as log:
    while True:
        temp = read_temp()
        cpu_temp = cpu.temperature
        print(temp, " " ,cpu_temp)
        log.write("{0},{1},{2}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp),str(cpu_temp)))
        sleep(10)
