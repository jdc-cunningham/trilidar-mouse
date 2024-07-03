#!/usr/bin/python

# MIT License
# 
# Copyright (c) 2017 John Bryan Moore
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import time
import VL53L0X
import RPi.GPIO as GPIO

# GPIO for Sensor 1 shutdown pin
sensor1_shutdown = 17
# GPIO for Sensor 2 shutdown pin
sensor2_shutdown = 27

sensor3_shutdown = 22

GPIO.setwarnings(False)

# Setup GPIO for shutdown pins on each VL53L0X
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor1_shutdown, GPIO.OUT)
GPIO.setup(sensor2_shutdown, GPIO.OUT)
GPIO.setup(sensor3_shutdown, GPIO.OUT)

# Set all shutdown pins low to turn off each VL53L0X
GPIO.output(sensor1_shutdown, GPIO.LOW)
GPIO.output(sensor2_shutdown, GPIO.LOW)
GPIO.output(sensor3_shutdown, GPIO.LOW)

# Keep all low for 500 ms or so to make sure they reset
time.sleep(0.50)

# Create one object per VL53L0X
tof = VL53L0X.VL53L0X(i2c_bus=1,i2c_address=0x29)
tof1 = VL53L0X.VL53L0X(i2c_bus=1,i2c_address=0x29)
tof2 = VL53L0X.VL53L0X(i2c_bus=1,i2c_address=0x29)

# Set shutdown pin high for the first VL53L0X
GPIO.output(sensor1_shutdown, GPIO.HIGH)
time.sleep(1)
# Set new address for the first VL53L0X
tof.change_address(0x2B)

# Set shutdown pin high for the second VL53L0X
# GPIO.output(sensor1_shutdown, GPIO.LOW)
GPIO.output(sensor2_shutdown, GPIO.HIGH)
time.sleep(1)
# Set new address for the second VL53L0X
tof1.change_address(0x2D)

# Set shutdown pin high for the third VL53L0X
# GPIO.output(sensor2_shutdown, GPIO.LOW)
GPIO.output(sensor3_shutdown, GPIO.HIGH)
time.sleep(1)
# Set new address for the third VL53L0X
tof2.change_address(0x2F)

# all high
# GPIO.output(sensor1_shutdown, GPIO.HIGH)
# GPIO.output(sensor2_shutdown, GPIO.HIGH)
# GPIO.output(sensor3_shutdown, GPIO.LOW)

# start ranging
tof.open()
time.sleep(0.50)
tof.start_ranging(VL53L0X.Vl53l0xAccuracyMode.HIGH_SPEED)

# start ranging
tof1.open()
time.sleep(0.50)
tof1.start_ranging(VL53L0X.Vl53l0xAccuracyMode.HIGH_SPEED)

# start ranging
tof2.open()
time.sleep(0.50)
tof2.start_ranging(VL53L0X.Vl53l0xAccuracyMode.HIGH_SPEED)

timing = tof.get_timing()
if timing < 20000:
    timing = 20000
print("Timing %d ms" % (timing/1000))

count = 0

while True:
    count += 1
    distance1 = tof.get_distance()
    # if distance > 0:
    #     print("sensor %d - %d mm, %d cm, iteration %d" % (1, distance, (distance/10), count))
    # else:
    #     print("%d - Error" % 1)

    distance2 = tof1.get_distance()

    # if distance > 0:
    #     print("sensor %d - %d mm, %d cm, iteration %d" % (2, distance, (distance/10), count))
    # else:
    #     print("%d - Error" % 2)

    distance3 = tof2.get_distance()
    # if distance > 0:
    #     print("sensor %d - %d mm, %d cm, iteration %d" % (3, distance, (distance/10), count))
    # else:
    #     print("%d - Error" % 3)

    print('top ' + str(distance1) + ', ' + 'left ' + str(distance2) + ', ' + 'right ' + str(distance3))

    time.sleep(timing/1000000.00)

tof.stop_ranging()
GPIO.output(sensor1_shutdown, GPIO.LOW)
tof1.stop_ranging()
GPIO.output(sensor2_shutdown, GPIO.LOW)
tof2.stop_ranging()
GPIO.output(sensor3_shutdown, GPIO.LOW)

tof.close()
tof1.close()