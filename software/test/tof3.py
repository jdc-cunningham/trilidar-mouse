# https://github.com/johnbryanmoore/VL53L0X_rasp_python/blob/master/python/VL53L0X_example.py
import time
import sys

sys.path.append('/home/pi/projects/trilidar-mouse/software/test/VL53L0X_rasp_python')

from python import VL53L0X_0
from python import VL53L0X_1
from python import VL53L0X_5

# Create a VL53L0X object
tof1 = VL53L0X_1.VL53L0X() # top
# tof2 = VL53L0X_0.VL53L0X() # right
# tof3 = VL53L0X_5.VL53L0X() # left

# change buses
# tof2.set_bus(0)
# tof3.set_bus(5)

# I2C Address can change before tof.open()
# tof.change_address(0x32)
# tof1.open()
# tof2.open()
# tof3.open()

# print('bus 1 ' + str(tof1.get_bus()) + ' dev ' + str(tof1.get_dev()))
# print('bus 2 ' + str(tof2.get_bus()) + ' dev ' + str(tof2.get_dev()))
# print('bus 3 ' + str(tof3.get_bus()) + ' dev ' + str(tof3.get_dev()))

# Start ranging
tof1.start_ranging(VL53L0X_1.VL53L0X_HIGH_SPEED_MODE) # high speed for 20ms
# tof2.start_ranging(VL53L0X_0.VL53L0X_HIGH_SPEED_MODE)
# tof3.start_ranging(VL53L0X_5.VL53L0X_HIGH_SPEED_MODE)

timing = tof1.get_timing()

if timing < 20000:
    timing = 20000
print("Timing %d ms" % (timing/1000))

def to_in(cm):
  return cm * 0.393701

count = 0

d1a = []
d2a = []
d3a = []

while True:
    count += 1
    distance1 = tof1.get_distance()

    # if distance1 > 0:
    #     print("top %d mm, %d cm, %d in, %d" % (distance1, (distance1/10), to_in(distance1 / 10), count))
    
    # distance2 = tof2.get_distance()

    # if distance2 > 0:
    #     print("left %d mm, %d cm, %d in, %d" % (distance2, (distance2/10), to_in(distance2 / 10), count))
    
    # distance3 = tof3.get_distance()
    
    # if distance3 > 0:
    #     print("right %d mm, %d cm, %d in, %d" % (distance3, (distance3/10), to_in(distance3 / 10), count))

    d1 = to_in(distance1 / 10)
    # d2 = to_in(distance2 / 10)
    # d3 = to_in(distance3 / 10)

    # print(str(d1) + ', ' + str(d2) + ', ' + str(d3))

    if (len(d1a) < 3):
        d1a.append(d1)
        # d2a.append(d2)
        # d3a.append(d3)
    else:
        d1a.pop(0)
        d2a.pop(0)
        d3a.pop(0)

        d1a.append(d1)
        # d2a.append(d2)
        # d3a.append(d3)

        d1av = round((sum(d1a) / 3), 2)
        # d2av = round((sum(d2a) / 3), 2)
        # d3av = round((sum(d3a) / 3), 2)

        # print('top ' + str(d1av) + ', ' + 'left ' + str(d3av) + ', ' + 'right ' + str(d2av))
        print(str(d1av))

    time.sleep(0.1)

    # time.sleep(timing/1000000.00)
