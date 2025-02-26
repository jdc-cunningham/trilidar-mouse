# https://github.com/johnbryanmoore/VL53L0X_rasp_python/blob/master/python/VL53L0X_example.py
import time
import sys

sys.path.append('/home/pi/projects/trilidar-mouse/software/test/VL53L0X-python')

from python import VL53L0X

def get_distance():
  tof = VL53L0X.VL53L0X(i2c_bus=1, i2c_address=0x29)
  tof.open()
  tof.start_ranging(VL53L0X.Vl53l0xAccuracyMode.BETTER)
  distance = tof.get_distance()
  tof.stop_ranging()
  return (distance / 10) * 0.39 # cm to in (1 -> 0.393701)

print(get_distance())
