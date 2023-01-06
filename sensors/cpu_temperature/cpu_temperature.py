'''
This script reads the cpu-temp.
'''

from time import sleep, strftime, time
from gpiozero import CPUTemperature

def get_temp():
    return CPUTemperature().temperature

if __name__ == '__main__':
    while True:
        print(get_temp())
        sleep(3)
