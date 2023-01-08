# NOTE: The import has a _ not - in the module name.
from pigpio_dht import DHT11
from time import sleep, strftime, time

temp_channel = 21 # BCM Numbering (this is the NAME)
sensor = DHT11(temp_channel, use_internal_pullup=True, timeout_secs = 1)

def get_temp_humidity():
    data = sensor.read(retries = 3)
    temp = data['temp_c']
    humidity = data['humidity']
    valid = data['valid']
    return temp, humidity, valid

if __name__ == '__main__':
    filename = 'data.csv'
    sleep_time = 60*15
    while True:
        with open(filename, 'a') as log:
            temp, humidity, valid = get_temp_humidity()
            log.write("{0},{1},{2},{3}\n".format(strftime("%H:%M"), str(temp), str(humidity),str(valid)))
        sleep(sleep_time)
