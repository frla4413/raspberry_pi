This is a digital sensor that can read the temperature and the relative humidity.
Tutorial:
  o Python library: https://pypi.org/project/pigpio-dht/

Wiering:
  o VCC (RED) to  5V
  o GND (BLACK) to GNDand
  o DATA (BLUE) to GPIO21
  o No need fo pull-up resistor (it is built in)

Works when measuring the room temperature and humidity
Remember to at least a sec, sleep(1), between measurments, dht11 are slow.
