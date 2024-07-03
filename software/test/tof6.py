# https://github.com/johnbryanmoore/VL53L0X_rasp_python/blob/master/python/VL53L0X_example.py
import sys

sys.path.append('/home/pi/projects/trilidar-mouse/software/test/VL53L0X-python')

import time
from python import VL53L0X
import RPi.GPIO as GPIO

toft_shutdown = 17
tofl_shutdown = 27
tofr_shutdown = 22

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(toft_shutdown, GPIO.OUT)
GPIO.setup(tofl_shutdown, GPIO.OUT)
GPIO.setup(tofr_shutdown, GPIO.OUT)

# Set all shutdown pins low to turn off each VL53L0X
GPIO.output(toft_shutdown, GPIO.LOW)
GPIO.output(tofl_shutdown, GPIO.LOW)
GPIO.output(tofr_shutdown, GPIO.LOW)

# Keep all low for 500 ms or so to make sure they reset
time.sleep(0.50)

# Create one object per VL53L0X passing the address to give to
# each.
tof = VL53L0X.VL53L0X(i2c_bus=1,i2c_address=0x2B) # 43
tof.open()
# tofl = VL53L0X.VL53L0X(address=0x2C) # 44
# tofr = VL53L0X.VL53L0X(address=0x29) # 45

# Set shutdown pin high for the first VL53L0X then 
# call to start ranging 
GPIO.output(toft_shutdown, GPIO.HIGH)
time.sleep(0.50)
# tof.change_address(0x2B)

tof.start_ranging(VL53L0X.Vl53l0xAccuracyMode.HIGH_SPEED)
tof.open()

# Set shutdown pin high for the second VL53L0X then 
# call to start ranging 
# GPIO.output(tofl_shutdown, GPIO.HIGH)
time.sleep(0.50)
# tofl.start_ranging(VL53L0X.VL53L0X_HIGH_SPEED_MODE)

# GPIO.output(tofr_shutdown, GPIO.HIGH)
# time.sleep(0.50)
# tofr.start_ranging(VL53L0X.VL53L0X_HIGH_SPEED_MODE)

timing = tof.get_timing()
if (timing < 20000):
    timing = 20000
print ("Timing %d ms" % (timing/1000))

for count in range(1,101):
    distance = tof.get_distance()
    if distance > 0:
        print("sensor %d - %d mm, %d cm, iteration %d" % (1, distance, (distance/10), count))
    else:
        print("%d - Error" % 1)

    # distance = tof.get_distance()
    # if distance > 0:
    #     print("sensor %d - %d mm, %d cm, iteration %d" % (2, distance, (distance/10), count))
    # else:
    #     print("%d - Error" % 2)

    time.sleep(timing/1000000.00)

tof.stop_ranging()
GPIO.output(toft_shutdown, GPIO.LOW)
# tofl.stop_ranging()
# GPIO.output(tofl_shutdown, GPIO.LOW)
# tofr.stop_ranging()
# GPIO.output(tofr_shutdown, GPIO.LOW)