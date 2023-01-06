''' Example of how to read the cpu-temp and write it to a file.
'''
import sensors.cpu_temperature.cpu_temperature as cpu_temp
from time import sleep, strftime, time

path = "data.csv"
with open(path, "a") as log:
    while True:
        temp = cpu_temp.get_temp()
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))
        sleep(3)
